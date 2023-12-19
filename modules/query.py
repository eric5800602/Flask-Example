from app import app
from flask import request
from pymongo import MongoClient


client = MongoClient('mongodb.railway.internal', 27017)

db = client.test
todos = db.request

@app.route('/send')
def send():
    try:
        req = request.get_json()
        user = req['user']
        request_name = req['request_name']
        post_id = todos.insert_one({user:request_name}).inserted_id
        return "Got request " + post_id
    except:
        return "Request fail"


@app.route('/query')
def query():
    args = todos.find_one()
    todos.DeleteOne(args)
    return args
