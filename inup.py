from pymongo import MongoClient
import os
from flask import jsonify
from sales import checkuser


def signin(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        return jsonify({"status": "success", "message": "welcome to {} {}".format(user["fname"], user["lname"]), "fname": user["fname"], "lname": user["lname"], "email": user["email"], "password": user["password"]})
    else:
        return jsonify({"status": "error", "message": "you don't exist, you could sign up in the sign-up page, or try again"})


def signup(request):
    info = request.json
    if info.get("password") and info.get("fname") and info.get("lname") and info.get("email"):
        password = os.environ.get("password")
        link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
        client = MongoClient(link)
        db = client.get_database('myAuctionDB')
        users = db.users
        if not users.find_one({'email': info.get("email").lower()}):
            user = {
                "fname": info.get("fname"),
                "lname": info.get("lname"),
                "email": info.get("email").lower(),
                "password": info.get("password"),
                "sales": [],
                "offers": [],
                "saved": []
            }
            users.insert_one(user)
            return jsonify({"status": "success", "message": " welcome to {} {} ".format(info.get("fname"), info.get("lname").lower())})
        else:
            return jsonify({"status": "error", "message": "you already exist"})
    else:
        return jsonify({"status": "error", "message": "you are missing some arguments"})


def delete(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        user = users.find_one({"email": info.get("email").lower(), "password": info.get("password")})
        for id in user["sales"]:
                sales.delete_one({"saleid": int(id)})
        users.delete_one({"email": info.get("email").lower(), "password": info.get("password")})
        return jsonify({"status": "success", "message": "you deleted {} account and it's sales, you could always sign up again".format(info.get("email").lower())})
    else:
        return jsonify({"status": "error", "message": "the {} account does not exist".format(info.get("email").lower())})

