from bson import ObjectId
from flask import jsonify
from funcs import checkuser, connect
import smtplib
from email.message import EmailMessage
import os


def signin(request):
    info = request.json
    db = connect()
    users = db.users
    if checkuser(info.get("email"), info.get("password"), users):
        user = users.find_one({'email': info.get("email"), 'password': info.get("password")})
        return jsonify({"status": "success", "message": "Welcome to {} {}.".format(user["fname"], user["lname"]),
                        "fname": user["fname"], "lname": user["lname"], "email": user["email"],
                        "password": user["password"]})
    else:
        return jsonify({"status": "error", "message": "Your username or password are incorrect."})


def signup(request):
    info = request.json
    if info.get("password") and info.get("fname") and info.get("lname") and info.get("email"):
        db = connect()
        users = db.users
        verify = db.verify
        if not (users.find_one({'email': info.get("email").lower()}) or verify.find_one({'email': info.get("email").lower()})):
            user = {
                "fname": info.get("fname"),
                "lname": info.get("lname"),
                "email": info.get("email").lower(),
                "password": info.get("password")
            }
            verify.insert_one(user)
            ver = verify.find_one(user)
            id= str(ver["_id"])
            msg = EmailMessage()
            msg['Subject'] = 'Welcome to Online Auction'
            msg["From"] = 'onlineauction176@gmail.com'
            msg['To'] = info.get("email")
            msg.add_alternative(f"""\
                <!DOCTYPE html>
                <html>
                    <body  style="background-color: #9c9c9c; text-align: center; padding:20px">
                        <h1>Welcome to Online Auction</h1>
                        <p>Hi {info.get("fname")}, this mail was sent to you because it was used to sign up to <a href="https://main--auctionlive.netlify.app/">Online Auction</a>, if was not done by you, please ignore it.</p>
                        <p>to verify your eamil please press <a href="https://onlineauctionapi.herokuapp.com/gotoverify/{id}">here</a></p>
                    </body>
                </html>
            """, subtype='html')

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login('onlineauction176@gmail.com', os.getenv("PASS"))

                smtp.send_message(msg)

            return jsonify({"status": "verify", "message": "go to your email to verify, and if you don't see it, check you spam to take it out of there."})
        else:
            return jsonify({"status": "error", "message": "you already exist"})
    else:
        return jsonify({"status": "error", "message": "you are missing some arguments"})


def gotoverify(id):
    return f"""\
        <!DOCTYPE html>
        <html>
            <body style="background-color: #9c9c9c; text-align: center; padding:20px">
                <h1>Welcome to Online Auction</h1>
                <form action="https://onlineauctionapi.herokuapp.com/verify" method="POST">
                    <label for="email">please enter your email.</label>
                    <input type="text" id="mail" name="mail"><br><br>
                    <input style="display: none !important;" type="text" id="id" name="id" value="{id}">
                    <input style="background-color: rgb(134, 163, 180); border-radius: 50px; height: 30px; max-width: 50%; min-width: 20%" type="submit" id="btn" value="Verify your account">
                </form>
            </body>
        </html>
    """


def verify(request):
    mail = request.form.get('mail')
    id = request.form.get('id')
    print(id)
    db = connect()
    users = db.users
    verify = db.verify
    if verify.find_one({"_id": ObjectId(id), "email": mail}):
        user = verify.find_one({"_id": ObjectId(id), "email": mail})
        del user["_id"]
        user["sales"] = []
        user["offers"] = []
        user["saved"] = []
        users.insert_one(user)
        verify.delete_one({"_id": ObjectId(id), "email": mail})
        return """\
                <!DOCTYPE html>
                <html>
                    <body style="background-color: #9c9c9c; text-align: center; padding:20px">
                        <h1>Welcome to Online Auction</h1>
                        <h2>Verification succeded</h2>
                        <p>Click <a href="https://main--auctionlive.netlify.app/">here</a> to go to the website.</p>
                    </body>
                </html>
            """
    else:
        return f"""\
                <!DOCTYPE html>
                <html>
                    <body style="background-color: #9c9c9c; text-align: center; padding:20px">
                        <h1>Welcome to Online Auction<h1>
                        <h2>Either you already have a account, or you didn't sign up.<h2>
                        <p>Click <a href="https://main--auctionlive.netlify.app/">here</a> to go to the website.</p>
                    </body>
                </html>
            """


def delete(request):
    info = request.json
    db = connect()
    users = db.users
    verify = db.verify
    if checkuser(info.get("email"), info.get("password"), users):
        user = users.find_one({"email": info.get("email").lower(), "password": info.get("password")})
        sales = db.sales
        chat = db.chat
        for id in user["sales"]:
            s = sales.find_one({"_id": ObjectId(id)})
            ch = s["chat"]
            chat.delete_one({"_id": ObjectId(ch)})
            sales.delete_one({"_id": ObjectId(id)})
        users.delete_one({"email": info.get("email").lower(), "password": info.get("password")})
        if verify.find_one({"email": info.get("email").lower(), "password": info.get("password")}):
            verify.delete_one({"_id": ObjectId(id)})
        return jsonify({"status": "success",
                        "message": "you deleted {} account and it's sales, you could always sign up again".format(
                            info.get("email").lower())})
    else:
        return jsonify(
            {"status": "error", "message": "the {} account does not exist".format(info.get("email").lower())})

