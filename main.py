from flask import Flask, jsonify, request
from flask.json import load
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from werkzeug.wrappers import response
from bson.json_util import dumps, ObjectId
import db_config as database

#Resources
from res.badge import Badge
from res.badges import Badges

app=Flask(__name__)
api=Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age':{'$gte':21}}))

    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response)

@app.route('/all/projection/')
def get_name_and_age():
    response = list(database.db.Badges.find({'age': {'$gte' : 21}}, {'name':1,'age':1}))

    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response)

@app.route('/all/kids/')
def get_kids():
    response = list(database.db.Badges.find({'age':{'$lte':21}}))

    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response)

@app.route('/all/names/')
def get_names():
    response = list(database.db.Badges.find({},{'name':1}))

    for document in response:
        document['_id'] = str(document['_id'])

    return jsonify(response)


api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')
api.add_resource(Badges, '/all/', '/del/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)