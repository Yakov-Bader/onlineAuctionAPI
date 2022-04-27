# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# add git huks

from flask import Flask, request, render_template, jsonify
from pip._internal.vcs import git
#from flask.wrappers import Response
#from py.prime import makePrime
#from galton import galtonboard
import git  # GitPython library
import os

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
    return jsonify({"chaim": "yakov"})
