from pymongo import MongoClient
import os
from flask import jsonify


def signin(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if users.find_one({'email': info.get("email").lower(), 'password': info.get("password")}):
        return jsonify({"status": "success", "message": "always nice to see you back"})
    else:
        return jsonify({"status": "error", "message": "you don't exist, i need a link to the sign up page"})


def signup(request):
    info = request.json
    if info.get("password") and info.get("name") and info.get("email"):
        password = os.environ.get("password")
        link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
        client = MongoClient(link)
        db = client.get_database('myAuctionDB')
        users = db.users
        if not users.find_one({'email': info.get("email").lower()}):
            user = {
                "name": info.get("name"),
                "email": info.get("email").lower(),
                "password": info.get("password"),
                "sales": [],
                "offers": [],
                "saved": []
            }
            users.insert_one(user)
            return jsonify({"status": "success", "message": " welcome to {} {} ".format(info.get("name"), info.get("email").lower())})
        else:
            return jsonify({"status": "error", "message": "you already exist"})
    else:
        return jsonify({"status": "error", "message": "you are missing some arguments"})