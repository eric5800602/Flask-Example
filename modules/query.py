from app import app
from flask import request
from pymongo import MongoClient


client = MongoClient('mongodb://mongo:1fDDeD6E35H4FbhHaDeEfCFaBFF6b15d@mongodb.railway.internal:27017')

db = client.test
todos = db.request

@app.route('/send',methods=['POST'])
def send():
    try:
        req = request.get_json()
        user = req['user']
        group_name = req['group_name']
        todos.insert_one({"user":user, "group_name":group_name})
        return "Got request "
    except:
        return "Request fail", 400


@app.route('/query')
def query():
    args = todos.find_one()
    try:
        if args:
            todos.delete_one({'_id': args['_id']})
            print(args)
            response = {"user":args["user"], "group_name":args["group_name"]}
            return response
        return "None request"
    except:
        return "Request fail",400
