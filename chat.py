from flask import jsonify
from flask_socketio import *
from funcs import checkuser, connect
from bson import ObjectId


def message(request):
    info = request.json
    db = connect()
    chat = db.chat
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        if chat.find_one({"_id": ObjectId(info.get("id"))}):
            msg = {
                "content": info.get("content"),
                "time": info.get("time"),
                "who": info.get("email")
            }
            chat.update_one({"_id": ObjectId(info.get("id"))}, {"$push": {"msg": msg}})
            return jsonify({"status": "success", "message": "grate, your message was sent"})
        else:
            return jsonify({"status": "error", "message": "cant find this chat"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def getChat(request):
    info = request.json
    db = connect()
    chat = db.chat
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        if chat.find_one({"_id": ObjectId(info.get("id"))}):
            ch = chat.find_one({"_id": ObjectId(info.get("id"))})
            return jsonify({"status": "success", "message": ch["msg"]})
        else:
            return jsonify({"status": "error", "message": "cant find this chat"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', to=room)
    # return the chat


def leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


def send(data):
    message = data['message']
    room = data['room']
    send(message, to=room)
