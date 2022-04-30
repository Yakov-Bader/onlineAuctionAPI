import flask
from pymongo import MongoClient
import os
from flask import jsonify


def sales(request):
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    sales = db.sales
    if flask.request.method == 'GET':
        results = []
        for s in sales.find({}, {"_id": 0}).limit(10):
            results.append(s)
        return jsonify(results)
    if flask.request.method == 'POST':
        info = request.args
        if not(info["admin"] and info["image"] and info["details"] and info["name"] and info["price"]):
            return jsonify({"status": "error", "message": "you are missing some details"})
        # might need to change to form not args
        saleid = int(os.environ.get("saleID"))+1
        saleid = str(saleid)

        sale = {
            "saleid": saleid,
            "admin": info["admin"],
            "chat": "chat id",
            "image": info["image"],
            "details": info["details"],
            "high": "no one gave a bid yet",
            "name": info["name"],
            "price": info["price"],
            "sold": False
        }
        sales.insert_one(sale)
        return jsonify({"status": "ok", "message": "you have crated a new sale"})


def bid(request):
    info = request.args
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    if users.find_one({'email': info["email"], 'password': info["password"]}):
        sales = db.sales
        sale = sales.find_one({"saleid": info["saleid"]})
        if sale["price"] < float(info["price"]):
            sales.update_one({"saleid": info["saleid"]}, {"$set": {"high": info["email"], "price": float(info["price"])}})
            return jsonify({"status": "ok", "message": "you have updated the sale"})
        else:
            return jsonify({"status": "error", "message": "you need to bid higher"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})
