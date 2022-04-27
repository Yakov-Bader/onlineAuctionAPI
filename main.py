# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
#add git huks

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"serh": "szgfdnsfg"})
