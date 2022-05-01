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
        info = request.args
        users = db.users
        if not (info["image"] and info["details"] and info["name"] and info["price"] and checkuser(info["admin"],
                                                                                                   info["password"],
                                                                                                   users)):
            return jsonify({"status": "error", "message": "you are missing some details or i don't recognize you"})
        if not sales.find_one({"name": info["name"], "admin": info["admin"].lower()}):
            saleid = db.id
            sid = saleid.find_one({})
            sid = sid["saleid"]
            saleid.update_one({"saleid": sid}, {"$set": {"saleid": sid + 1}})
            sale = {
                "saleid": sid,
                "admin": info["admin"].lower(),
                "chat": "chat id",
                "image": info["image"],
                "details": info["details"],
                "high": "no one gave a bid yet",
                "name": info["name"],
                "price": float(info["price"]),
                "sold": False
            }
            sales.insert_one(sale)
            users = db.users
            users.update_one({"email": info["admin"].lower()}, {"$push": {"sales": sid}})
            return jsonify({"status": "ok", "message": "you have crated a new sale"})
        else:
            return jsonify({"status": "error", "message": "you already have a sale with this name"})


def bid(request):
    info = request.args
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if checkuser(info["email"].lower(), info["password"], users):
        sales = db.sales
        sale = sales.find_one({"saleid": float(info["saleid"])})
        if sale["price"] < float(info["price"]):
            sales.update_one({"saleid": float(info["saleid"])},
                             {"$set": {"high": info["email"].lower(), "price": float(info["price"])}})
            users.update_one({"email": info["email"].lower()}, {"$push": {"offers": info["saleid"]}})
            return jsonify({"status": "ok", "message": "you have updated the sale"})
        else:
            return jsonify({"status": "error", "message": "you need to bid higher"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def like(request):
    info = request.args
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if info["email"] and info["id"]:
        if checkuser(info["email"].lower(), info["password"], users):
            if int(info["like"]) == 1:
                users.update_one({"email": info["email"].lower()}, {"$push": {"saved": info["id"]}})
                return jsonify({"status": "ok", "message": "your like was successful"})
            else:
                users.update_one({"email": info["email"].lower()}, {"$pull": {"saved": info["id"]}})
                return jsonify({"status": "ok", "message": "your remove like was successful"})
        else:
            return jsonify({"status": "error", "message": "I don't recognize you"})
    return jsonify({"status": "error", "message": "you are missing some details"})
