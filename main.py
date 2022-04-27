# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# add git huks

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
        mising = ""
        if not info["password"]:
            mising += " password "
        if not info["password2"]:
            mising += " password2 "
        if not info["name"]:
            mising += " name "
        if not info["email"]:
            mising += " email "

        return jsonify({"error": "you are missing arguments", "the arguments are ": mising})
    else:
        return jsonify({"request": "succeeded", "welcome to": info["name"]})
