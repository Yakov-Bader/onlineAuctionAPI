from pymongo import MongoClient
import os


def checkuser(email, password, users):
    if email and password:
        return users.find_one({'email': email.lower(), 'password': password})
    else:
        return False


def connect():
    password = os.environ.get("password")
    link = 'mongodb+srv://yakov:' + password + '@cluster0.irzzw.mongodb.net/myAuctionDB?retryWrites=true&w=majority'
    client = MongoClient(link)
    db = client.get_database('myAuctionDB')
    return db
