
# connect to mongoDB, connect to socket.io
import time

from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify
from pip._internal.vcs import git
import git
from pymongo import MongoClient
import os

app = Flask(__name__)

project_home = '/home/yakovbader/onlineAuctionAPI'
# project_home = 'onlineAuction'
project_folder = os.path.expanduser(project_home)
load_dotenv(os.path.join(project_folder, '.env'))


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./onlineAuctionAPI')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route('/')
def hello_world():

    return jsonify({"chaim shwartz 3": "yakov bader 2"})


@app.route('/signup', methods=['POST'])
async def signup():
    info = request.args
    if info["password"] == info["password2"] and info["name"] and info["email"] and info["password"] and info["password2"]:
        password = os.getenv("password")
        link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
        client = MongoClient(link)
        db = client.get_database('myAuctionDB')
        users = db.users
        await pushuser(users, info)
        return jsonify({"status": "ok", "message": " welcome to {} {} ".format(info["name"], info["email"])})
    else:
        return jsonify({"status": "error", "message": "you are missing some arguments"})


async def pushuser(users, info):
    return users.insert_one({
        'name': info["name"],
        'email': info["email"],
        'password': info["password"],
        'sales': [],
        'offers': [],
        'saved': []
    })

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)