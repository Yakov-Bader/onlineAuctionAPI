import flask
from flask import jsonify
from funcs import checkuser, connect


def sales(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if flask.request.method == 'GET':
        results = []
        for s in sales.find({}, {"_id": 0}).limit(9):
            user = users.find_one({"email": info.get("email"), "password": info.get("password")})
            s["admin"] = 0
            s["offers"] = 0
            s["saved"] = 0
            if str(s["saleid"]) in user["sales"]:
                s["admin"] = 1
            if str(s["saleid"]) in user["offers"]:
                s["offers"] = 1
            if str(s["saleid"]) in user["saved"]:
                s["saved"] = 1
            if not s["sold"]:
                results.append(s)
        response = {"status": "success", "message": results}
        return jsonify(response)
    if flask.request.method == 'POST':
        if checkuser(info.get("email"), info.get("password"), users):
            if not (info.get("image") and info.get("details") and info.get("name") and info.get("price")):
                return jsonify({"status": "error", "message": "you are missing some details"})
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
                return jsonify({"status": "success", "message": "you have crated a new sale"})
            else:
                return jsonify({"status": "error", "message": "you already have a sale with this name"})
        else:
            return jsonify({"status": "error", "message": "I don't recognize you"})


def bid(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("email").lower(), info.get("password"), users):
        sales = db.sales
        sale = sales.find_one({"saleid": float(info.get("id"))})
        if sale["price"] < float(info.get("price")):
            sales.update_one({"saleid": float(info.get("id"))},
                             {"$set": {"high": info.get("email").lower(), "price": float(info.get("price"))}})
            users.update_one({"email": info.get("email").lower()}, {"$push": {"offers": info.get("id")}})
            return jsonify({"status": "success", "message": "you have updated the sale"})
        else:
            return jsonify({"status": "error", "message": "you need to bid higher"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def like(request):
    info = request.json
    db = connect()
    users = db.users
    if info.get("email") and info.get("id"):
        if checkuser(info.get("email").lower(), info.get("password"), users):
            if int(info.get("like")) == 1:
                users.update_one({"email": info.get("email").lower()}, {"$push": {"saved": info.get("id")}})
                return jsonify({"status": "success", "message": "your like was successful"})
            else:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"saved": info.get("id")}})
                return jsonify({"status": "success", "message": "your remove like was successful"})
        else:
            return jsonify({"status": "error", "message": "I don't recognize you"})
    return jsonify({"status": "error", "message": "you are missing some details"})


def remove(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("email").lower(), info.get("password"), users):
        sales = db.sales
        if sales.find_one({"saleid": int(info.get("id"))}):
            name = sales.find_one({"saleid": int(info.get("id"))})["name"]
            sales.delete_one({"saleid": int(info.get("id"))})
            return jsonify({"status": "success", "message": "you removed the sale {}".format(name)})
        else:
            return jsonify({"status": "error", "message": "the sale does not exist"})
    return jsonify({"status": "error", "message": "I don't recognize you"})
