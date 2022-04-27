
# connect to mongoDB, connect to socket.io

from flask import Flask, request, render_template, jsonify
from pip._internal.vcs import git
import git

app = Flask(__name__)


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
    if not (info["password"] == info["password2"] and info["name"] and info["email"]):
        missing = " "
        if not info["password"]:
            missing.join(" password ")
        if not info["password2"]:
            missing.join(" password2 ")
        if not info["name"]:
            missing.join(" name ")
        if not info["email"]:
            missing.join(" email ")
        return jsonify({"status": "error", "message": "you are missing {}".format(missing)})
    else:
        return jsonify({"status": "ok", "message": " welcome to {} {} ".format(info["name"], info["email"])})
