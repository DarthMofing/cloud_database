from flask import Flask, json, jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
from werkzeug.wrappers import response
import db_config as database

class Posts(Resource):
    """Posts behavior"""

    def get(self, _id):
        response = self.abort_if_not_exist(_id)
        response[_id] = str(response['_id'])
        return jsonify(response)

    def post(self, _id):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({'_id':ObjectId(_id)},{'$push':{
            'post':{
                'id':request.json['id'],
                'name':request.json['name'],
                'img':request.json['img'],
                'date':request.json['date']
            }
        }})

        return jsonify({'message':f'The post {request.json["id"]} successfuly created'})

    def put(self,_id,uuid):
        response = self.abort_if_not_exist(_id)
        database.db.Badges.update_one({'_id':ObjectId(_id), 'post.id':uuid},
        {'$set':{
            'post.$.name':request.json['name'],
            'post.$.img':request.json['img'],
            'post.$.date':request.json['date']
        }
        })

        return jsonify(request.json)

    def abort_if_not_exist(self,_id):
        response = database.db.Badges.find_one({'_id':ObjectId(_id)}, {'name':1, "post":1})

        if response:
            return response
        else:
            abort(jsonify({'status':404, '_id':f'{_id} not found'}))
