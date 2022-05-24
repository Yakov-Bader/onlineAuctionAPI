import os
# web: gunicorn main:app
from inup import *
from my import *
from sales import *
from flask import Flask, request, render_template, jsonify
from flask_cors import cross_origin, CORS
from pip._internal.vcs import git
import git
from flask_socketio import SocketIO, send, emit


app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
socketio = SocketIO(app, cors_allowed_origins="*")


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./onlineAuctionAPI')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route('/')
@cross_origin('/', methods=['GET', 'POST'])
def hello_world():
    return jsonify({"status": "ok", "message": "send here a link to the sign up page"})


@app.route('/signup', methods=['POST'])
def signUp():
    return signup(request)


@app.route('/signin', methods=['POST'])
def signIn():
    return signin(request)


@app.route('/delete', methods=['POST'])
def Delete():
    return delete(request)


@app.route('/sales', methods=['POST'])
def Sales():
    return sales(request)


@app.route('/getsales', methods=['POST'])
def GetSales():
    return getsales(request)


@app.route('/bid', methods=['POST'])
def Bid():
    return bid(request)


@app.route('/like', methods=['POST'])
def Like():
    return like(request)


@app.route('/remove', methods=['POST'])
def Remove():
    return remove(request)


@app.route('/mysales', methods=['POST'])
def MySales():
    return mySales(request)


@app.route('/mysaved', methods=['POST'])
def MySaved():
    return mySaved(request)


@app.route('/myoffers', methods=['POST'])
def MyOffers():
    return myOffers(request)


@socketio.on('send')
def handleMessage(msg):
    print(msg['message'])
    emit('message', msg, broadcast=True)


@socketio.on('connect', namespace="/api")
@cross_origin()
def connect():
    sid = "sdfgm"
    print('connected ' + sid)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
    # app.run(host='localhost', port=5000, debug=True)
