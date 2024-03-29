from bson import ObjectId
from flask import jsonify
from funcs import checkuser, connect


def mySales(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        mysales = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        mysalesid = user["sales"]
        if not mysalesid:
            return jsonify({"status": "error", "message": "you did not create a sale yet"})

        if info.get("amount"):
            if not str(info.get("amount")).isnumeric():
                return jsonify({"status": "error", "message": "you need to give a valid number"})
            else:
                if info.get("amount") == "0":
                    amount = len(mysalesid)
                else:
                    amount = int(info.get("amount"))
        else:
            amount = 9
        for id in mysalesid[0:amount]:
            sale = sales.find_one({"_id": ObjectId(id)})
            if not sale:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"sales": id}})
                continue
            sale["saleid"] = str(sale["_id"])
            del sale["_id"]
            sale["isadmin"] = True
            sale["offers"] = False
            sale["saved"] = False
            if sale["saleid"] in user["saved"]:
                sale["saved"] = True
            if sale["saleid"] in user["offers"]:
                sale["offers"] = True
            mysales.append(sale)
        response = {"status": "success", "message": mysales}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def mySaved(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        mysaved = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        mysavedid = user["saved"]
        if not mysavedid:
            return jsonify({"status": "error", "message": "you have no saved sales"})

        if info.get("amount"):
            if not str(info.get("amount")).isnumeric():
                return jsonify({"status": "error", "message": "you need to give a valid number"})
            else:
                if info.get("amount") == "0":
                    amount = len(mysavedid)
                else:
                    amount = int(info.get("amount"))
        else:
            amount = 9
        for id in mysavedid[0:amount]:
            sale = sales.find_one({"_id": ObjectId(id)})
            if not sale:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"saved": id}})
                continue
            sale["saleid"] = str(sale["_id"])
            del sale["_id"]
            sale["isadmin"] = False
            sale["offers"] = False
            sale["saved"] = True
            if sale["saleid"] in user["sales"]:
                sale["isadmin"] = True
            if sale["saleid"] in user["offers"]:
                sale["offers"] = True
            mysaved.append(sale)
        response = {"status": "success", "message": mysaved}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def myOffers(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        myoffers = []
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        myoffersid = user["offers"]
        if not myoffersid:
            return jsonify({"status": "error", "message": "you did not bid on a sale yet"})

        if info.get("amount"):
            if not str(info.get("amount")).isnumeric():
                return jsonify({"status": "error", "message": "you need to give a valid number"})
            else:
                if info.get("amount") == "0":
                    amount = len(myoffersid)
                else:
                    amount = int(info.get("amount"))
        else:
            amount = 9
        for id in myoffersid[0:amount]:
            sale = sales.find_one({"_id": ObjectId(id)})
            if not sale:
                users.update_one({"email": info.get("email").lower()}, {"$pull": {"offers": id}})
                continue
            sale["saleid"] = str(sale["_id"])
            del sale["_id"]
            sale["isadmin"] = False
            sale["offers"] = True
            sale["saved"] = False
            if sale["saleid"] in user["saved"]:
                sale["saved"] = True
            if sale["saleid"] in user["sales"]:
                sale["isadmin"] = True
            myoffers.append(sale)
        response = {"status": "success", "message": myoffers}
        return jsonify(response)
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def getProfile(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")},
                              {"_id": 0, "offers": 0, "sales": 0, "saved": 0})
        print(user['fname'])
        return jsonify({"status": "success", "message": user})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def updateProfile(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        users.update_one({"email": info.get("email").lower()}, {
            "$set": {"fname": info.get("newname"), "lname": info.get("newlast"), "password": info.get("newpass")}})
        return jsonify({"status": "success", "message": "you have just updated you profile"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})


def sell(request):
    info = request.json
    db = connect()
    users = db.users
    sales = db.sales
    if checkuser(info.get("email"), info.get("password"), users):
        if users.find_one({"sales": info.get("id"), "email": info.get("email"), "password": info.get("password")}):
            sales.update_one({"_id": ObjectId(info.get("id"))}, {"$set": {"sold": True}})
            sale = sales.find_one({"_id": ObjectId(info.get("id"))})
            return jsonify({"status": "success", "message": "you have just sold the sale to {}".format(sale["high"])})
        else:
            return jsonify({"status": "error", "message": "you dont own this sale"})
    else:
        return jsonify({"status": "error", "message": "I don't recognize you"})
