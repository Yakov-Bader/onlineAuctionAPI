import flask
from pymongo import MongoClient
import os
from flask import jsonify


def checkuser(email, password, users):
    if email and password:
        return users.find_one({'email': email.lower(), 'password': password})
    else:
        return False


def sales(request):
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    sales = db.sales
    if flask.request.method == 'GET':
        results = []
        for s in sales.find({}, {"_id": 0}).limit(10):
            if not s["sold"]:
                results.append(s)
        return jsonify(results)
    if flask.request.method == 'POST':
        # might need to change to form not args
        info = request.json
        users = db.users
        if not (info.get("image") and info.get("details") and info.get("name") and info.get("price") and checkuser(info.get("admin"),
                                                                                                   info.get("password"),
                                                                                                   users)):
            return jsonify({"status": "error", "message": "you are missing some details or i don't recognize you"})
        if not sales.find_one({"name": info.get("name"), "admin": info.get("admin").lower()}):
            saleid = db.id
            sid = saleid.find_one({})
            sid = sid["saleid"]
            saleid.update_one({"saleid": sid}, {"$set": {"saleid": sid + 1}})
            sale = {
                "saleid": sid,
                "admin": info.get("admin").lower(),
                "chat": "chat id",
                "image": info.get("image"),
                "details": info.get("details"),
                "high": "no one gave a bid yet",
                "name": info.get("name"),
                "price": float(info.get("price")),
                "sold": False
            }
            sales.insert_one(sale)
            users = db.users
            users.update_one({"email": info.get("admin").lower()}, {"$push": {"sales": sid}})
            return jsonify({"status": "ok", "message": "you have crated a new sale"})
        else:
            return jsonify({"status": "error", "message": "you already have a sale with this name"})


def bid(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if checkuser(info.get("email").lower(), info.get("password"), users):
        sales = db.sales
        sale = sales.find_one({"saleid": float(info.get("saleid"))})
        if sale["price"] < float(info.get("price")):
            sales.update_one({"saleid": float(info.get("saleid"))},
                             {"$set": {"high": info.get("email").lower(), "price": float(info.get("price"))}})
            users.update_one({"email": info.get("email").lower()}, {"$push": {"offers": info.get("saleid")}})
            return jsonify({"status": "ok", "message": "you have updated the sale"})
        else:
            return jsonify({"status": "error", "message": "you need to bid higher"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def like(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if info.get("email") and info.get("id"):
        if checkuser(info.get("email").lower(), info.get("password"), users):
            if int(info.get("like")) == 1:
                users.update_one({"email": info.get("email").lower()}, {"$push": {"saved": info.get("id")}})
                return jsonify({"status": "ok", "message": "your like was successful"})
            else:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"saved": info.get("id")}})
                return jsonify({"status": "ok", "message": "your remove like was successful"})
        else:
            return jsonify({"status": "error", "message": "I don't recognize you"})
    return jsonify({"status": "error", "message": "you are missing some details"})
