from inup import *
from my import *
from sales import *
from chat import *
from flask import Flask, request, jsonify
from flask_cors import cross_origin, CORS
import git
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/git_update', methods=['POST'])
def git_update():
    repo = git.Repo('./onlineAuctionAPI')
    origin = repo.remotes.origin
    repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
    origin.pull()
    return '', 200


@app.route('/')
@cross_origin('/', methods=['GET', 'POST'])
def hello_world():
    return jsonify({"status": "ok", "message": "send here a link to the sign up page"})


@app.route('/signup', methods=['POST'])
def Signup():
    return signup(request)


@app.route('/verify', methods=['POST', 'GET'])
def Verify():
    return verify(request)


@app.route('/gotoverify/<id>', methods=['POST', 'GET'])
def GoToVerify(id):
    return gotoverify(id)


@app.route('/signin', methods=['POST'])
def signIn():
    return signin(request)


@app.route('/delete', methods=['POST'])
def Delete():
    return delete(request)


@app.route('/sales', methods=['POST'])
def Sales():
    return sales(request)


@app.route('/getsale', methods=['POST'])
def GetSales():
    return getsale(request)


@app.route('/getsales', methods=['POST'])
def GetSale():
    return getsales(request)


@app.route('/bid', methods=['POST'])
def Bid():
    return bid(request)


@app.route('/like', methods=['POST'])
def Like():
    return like(request)


@app.route('/remove', methods=['POST'])
def Remove():
    return remove(request)


@app.route('/mysales', methods=['POST'])
def MySales():
    return mySales(request)


@app.route('/mysaved', methods=['POST'])
def MySaved():
    return mySaved(request)


@app.route('/myoffers', methods=['POST'])
def MyOffers():
    return myOffers(request)


@app.route('/getprofile', methods=['POST'])
def GetProfile():
    return getProfile(request)


@app.route('/updateprofile', methods=['POST'])
def UpdateProfile():
    return updateProfile(request)


@app.route('/message', methods=['POST'])
def Message():
    return message(request)


@app.route('/getchat', methods=['POST'])
def GetChat():
    return getChat(request)


@app.route('/sell', methods=['POST'])
def Sell():
    return sell(request)


if __name__ == '__main__':
    app.run(debug=True)
