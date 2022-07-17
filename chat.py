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
            user = users.find_one({'email': info.get("email"), 'password': info.get("password")}, {"_id": 0, "offers": 0, "sales": 0, "saved": 0})
            msg = {
                "content": info.get("content"),
                "time": info.get("time"),
                "who": info.get("email"),
                "name": user['fname']+" "+user['lname']
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


def leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', to=room)


def send(data):
    message = data['message']
    room = data['room']
    send(message, to=room)
