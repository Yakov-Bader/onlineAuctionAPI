from pymongo import MongoClient
import os
from flask import jsonify


def signin(request):
    # might need to change to form not args
    info = request.args
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if users.find_one({'email': info["email"].lower(), 'password': info["password"]}):
        return jsonify({"status": "ok", "message": " welcome, here i need a link to the website, for render :)"})
    else:
        return jsonify({"status": "error", "message": "you dont exist, i need a link to the sign up page"})


def signup(request):
    return "sdfghjk"
    # might need to change to form not args
    info = request.args
    if info["password"] and info["name"] and info["email"]:
        password = os.environ.get("password")
        link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
        client = MongoClient(link)
        db = client.get_database('myAuctionDB')
        users = db.users
        if not users.find_one({'email': info["email"].lower()}):
            user = {
                "name": info["name"],
                "email": info["email"].lower(),
                "password": info["password"],
                "sales": [],
                "offers": [],
                "saved": []
            }
            users.insert_one(user)
            return jsonify({"status": "ok", "message": " welcome to {} {} ".format(info["name"], info["email"].lower())})
        else:
            return jsonify({"status": "error", "message": "you already exist"})
    else:
        return jsonify({"status": "error", "message": "you are missing some arguments"})