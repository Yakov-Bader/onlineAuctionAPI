from flask_socketio import *


def connect():
    print("connected")


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
