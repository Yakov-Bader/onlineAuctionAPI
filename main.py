# connect to socket.io
import flask
from inup import signin, signup
from sales import sales, bid
from flask import Flask, request, render_template, jsonify

from pip._internal.vcs import git
import git
from pymongo import MongoClient
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
    return jsonify({"status": "ok", "message": "send here a link to the sign up page"})


@app.route('/signup', methods=['POST'])
def signUp():
    return signup(request)


@app.route('/signin')
def signIn():
    return signin(request)


@app.route('/sales', methods=['GET', 'POST'])
def Sales():
    return sales(request)


@app.route('/bid', methods=['POST'])
def Bid():
    return bid(request)


if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
