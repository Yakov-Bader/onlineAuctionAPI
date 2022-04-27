
# connect to mongoDB, connect to socket.io
from flask import Flask, request, render_template, jsonify
from pip._internal.vcs import git
import git
from pymongo import MongoClient

app = Flask(__name__)
password = " "
link = 'mongodb+srv://yakov:'+password+'@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
client = MongoClient(link)
db = client.get_database('myAuctionDB')
users = db.users
users.insert_one({})  # to add user
users.find({})
users.find_one({})
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
def signup():

    info = request.args
    if info["password"] == info["password2"] and info["name"] and info["email"] and info["password"] and info["password2"]:
        return jsonify({"status": "ok", "message": " welcome to {} {} ".format(info["name"], info["email"])})
    else:
        return jsonify({"status": "error", "message": "you are missing information"})
