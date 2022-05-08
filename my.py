import flask
from pymongo import MongoClient
import os
from flask import jsonify
from sales import checkuser


def mySales(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        mysales = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        mysalesid=user["sales"]
        for id in mysalesid:
            sale = sales.find_one({"saleid": float(id)}, {"_id": 0})
            mysales.append(sale)
        response = {"status": "success", "message": mysales}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def mySaved(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        mysaved = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        mysavedid = user["saved"]
        for id in mysavedid:
            sale = sales.find_one({"saleid": float(id)}, {"_id": 0})
            mysaved.append(sale)
        response = {"status": "success", "message": mysaved}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def myOffers(request):
    info = request.json
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        myoffers = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        myoffersid = user["offers"]
        for id in myoffersid:
            sale = sales.find_one({"saleid": float(id)}, {"_id": 0})
            myoffers.append(sale)
        response = {"status": "success", "message": myoffers}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})