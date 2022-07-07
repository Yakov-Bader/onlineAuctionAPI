from bson import ObjectId
from flask import jsonify
from funcs import checkuser, connect


def getsale(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        if sales.find_one({"_id": ObjectId(info.get("id"))}):
            s = sales.find_one({"_id": ObjectId(info.get("id"))})
            user = users.find_one({"email": info.get("email"), "password": info.get("password")})
            s["saleid"] = info.get("id")
            del s["_id"]
            s["isadmin"] = False
            s["offers"] = False
            s["saved"] = False
            if s["saleid"] in user["sales"]:
                s["isadmin"] = True
            if s["saleid"] in user["offers"]:
                s["offers"] = True
            if s["saleid"] in user["saved"]:
                s["saved"] = True
            if not s["sold"]:
                del s["sold"]
            return jsonify({"status": "success", "message": s})
        else:
            return jsonify({"status": "error", "message": "I don't recognize this sale"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def getsales(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        results = []
        if not str(info.get("amount")).isnumeric():
            return jsonify({"status": "error", "message": "you need to give a valid number"})
        for s in sales.find({}).limit(int(info.get("amount"))):
            print(s)
            user = users.find_one({"email": info.get("email"), "password": info.get("password")})
            s["saleid"] = str(s["_id"])
            del s["_id"]
            s["isadmin"] = False
            s["offers"] = False
            s["saved"] = False
            if s["saleid"] in user["sales"]:
                s["isadmin"] = True
            if s["saleid"] in user["offers"]:
                s["offers"] = True
            if s["saleid"] in user["saved"]:
                s["saved"] = True
            results.append(s)
        response = {"status": "success", "message": results}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def sales(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("admin"), info.get("password"), users):
        sales = db.sales
        if not (info.get("image") and info.get("details") and info.get("name") and info.get("price")):
            return jsonify({"status": "error", "message": "you are missing some details"})
        if not sales.find_one({"name": info.get("name"), "admin": info.get("admin").lower()}):
            chat = db.chat
            users = db.users
            c = {"msg": []}
            cid = chat.insert_one(c)
            sale = {
                "likes": [],
                "biders": [],
                "admin": info.get("admin").lower(),
                "chat": str(cid.inserted_id),
                "image": info.get("image"),
                "details": info.get("details"),
                "high": "no one gave a bid yet",
                "name": info.get("name"),
                "price": float(info.get("price")),
                "sold": False
            }
            sales.insert_one(sale)
            s = sales.find_one(sale)
            users.update_one({"email": info.get("admin").lower()}, {"$push": {"sales": str(s["_id"])}})
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
        sale = sales.find_one({"_id": ObjectId(info.get("id"))})
        if sale["price"] < float(info.get("price")):
            if not users.find_one({"email": info.get("email").lower(), "offers": info.get("id"), 'password': info.get("password")}):
                users.update_one({"email": info.get("email").lower()}, {"$push": {"offers": info.get("id")}})
            user = users.find_one({"email": info.get("email").lower(), 'password': info.get("password")})
            sales.update_one({"_id": ObjectId(info.get("id"))}, {"$set": {"high": info.get("email").lower(), "price": float(info.get("price"))}})
            sales.update_one({"_id": ObjectId(info.get("id"))}, {"$push": {"biders": user["fname"]+" "+user["lname"]}})
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
            sales = db.sales
            if info.get("like"):
                users.update_one({"email": info.get("email").lower()}, {"$push": {"saved": info.get("id")}})
                user = users.find_one({"email": info.get("email").lower(), 'password':info.get("password")})
                sales.update_one({"_id": ObjectId(info.get("id"))}, {"$push": {"likes": user["fname"]+" "+user["lname"]}})
                return jsonify({"status": "success", "message": "your like was successful"})
            else:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"saved": info.get("id")}})
                user = users.find_one({"email": info.get("email").lower(), 'password': info.get("password")})
                sales.update_one({"_id": ObjectId(info.get("id"))}, {"$pull": {"likes": user["fname"]+" " + user["lname"]}})
                return jsonify({"status": "success", "message": "your remove like was successful"})
        else:
            return jsonify({"status": "error", "message": "I don't recognize you"})
    return jsonify({"status": "error", "message": "you are missing some details"})


def remove(request):
    info = request.json
    db = connect()
    users = db.users
    if users.find_one({'email': info.get("email").lower(), 'password': info.get("password"), 'sales': info.get("id")}):
        sales = db.sales
        if sales.find_one({"_id": ObjectId(info.get("id"))}):
            chat = db.chat
            s = sales.find_one({"_id": ObjectId(info.get("id"))})
            name = s["name"]
            ch = s["chat"]
            chat.delete_one({"_id": ObjectId(ch)})
            sales.delete_one({"_id": ObjectId(info.get("id"))})
            return jsonify({"status": "success", "message": "you removed the sale {}".format(name)})
        else:
            return jsonify({"status": "error", "message": "the sale does not exist"})
    return jsonify({"status": "error", "message": "you are not the admin of this sale"})
