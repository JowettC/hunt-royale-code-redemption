from flask import Flask, jsonify, request
import datetime
import requests
from dotenv import load_dotenv
import os
from getCodes import getCodes
# print (sys.version)
load_dotenv()
token = os.getenv("token")


app = Flask(__name__)


def welcome_msg(item):
    global token
    if item["text"].lower() == "/getcodes":
        msg = 'hello'
        chat_id = item["chat"]["id"]
        user_id = item["from"]["id"]
        user_name = item["from"].get("username",user_id)
        welcome_msg = '''{}'''.format(msg)
        to_url = 'https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}&parse_mode=HTML'.format(token, chat_id, welcome_msg)
        resp = requests.get(to_url)


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        data = request.get_json()
        data = data["message"]
        welcome_msg(data)
        return { 'statusCode' : 200, 'body' : 'Success' , 'data' : data }
    else:
        return { 'statusCode' : 200, 'body' : 'Success'}