from flask import jsonify, request
from flask_restful import Resource, abort
from flask_pymongo import pymongo
from bson.json_util import ObjectId
import db_config as database

class Badges(Resource):
    '''Get all badges'''
    def get(self):
        response = list(database.db.Badges.find())

        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)

    def post(self):
        _ids = list(database.db.Badges.insert_many([
            {
                'name':request.json[0]['name'],
                'last_name':request.json[0]['last_name'],
                'profile_pic':request.json[0]['profile_pic'],
                'hero_badge':request.json[0]['hero_badge'],
                'age':request.json[0]['age'],
                'city':request.json[0]['city'],
                'followers':request.json[0]['followers'],
                'likes':request.json[0]['likes'],
                'posts':request.json[0]['posts'],
            },
            {
                'name':request.json[1]['name'],
                'last_name':request.json[1]['last_name'],
                'profile_pic':request.json[1]['profile_pic'],
                'hero_badge':request.json[1]['hero_badge'],
                'age':request.json[1]['age'],
                'city':request.json[1]['city'],
                'followers':request.json[1]['followers'],
                'likes':request.json[1]['likes'],
                'posts':request.json[1]['posts'],
            },
            {
                'name':request.json[2]['name'],
                'last_name':request.json[2]['last_name'],
                'profile_pic':request.json[2]['profile_pic'],
                'hero_badge':request.json[2]['hero_badge'],
                'age':request.json[2]['age'],
                'city':request.json[2]['city'],
                'followers':request.json[2]['followers'],
                'likes':request.json[2]['likes'],
                'posts':request.json[2]['posts'],
            },
            {
                'name':request.json[3]['name'],
                'last_name':request.json[3]['last_name'],
                'profile_pic':request.json[3]['profile_pic'],
                'hero_badge':request.json[3]['hero_badge'],
                'age':request.json[3]['age'],
                'city':request.json[3]['city'],
                'followers':request.json[3]['followers'],
                'likes':request.json[3]['likes'],
                'posts':request.json[3]['posts'],
            },
            {
                'name':request.json[4]['name'],
                'last_name':request.json[4]['last_name'],
                'profile_pic':request.json[4]['profile_pic'],
                'hero_badge':request.json[4]['hero_badge'],
                'age':request.json[4]['age'],
                'city':request.json[4]['city'],
                'followers':request.json[4]['followers'],
                'likes':request.json[4]['likes'],
                'posts':request.json[4]['posts'],
            },
            {
                'name':request.json[5]['name'],
                'last_name':request.json[5]['last_name'],
                'profile_pic':request.json[5]['profile_pic'],
                'hero_badge':request.json[5]['hero_badge'],
                'age':request.json[5]['age'],
                'city':request.json[5]['city'],
                'followers':request.json[5]['followers'],
                'likes':request.json[5]['likes'],
                'posts':request.json[5]['posts'],
            },
            {
                'name':request.json[6]['name'],
                'last_name':request.json[6]['last_name'],
                'profile_pic':request.json[6]['profile_pic'],
                'hero_badge':request.json[6]['hero_badge'],
                'age':request.json[6]['age'],
                'city':request.json[6]['city'],
                'followers':request.json[6]['followers'],
                'likes':request.json[6]['likes'],
                'posts':request.json[6]['posts'],
            },
            {
                'name':request.json[7]['name'],
                'last_name':request.json[7]['last_name'],
                'profile_pic':request.json[7]['profile_pic'],
                'hero_badge':request.json[7]['hero_badge'],
                'age':request.json[7]['age'],
                'city':request.json[7]['city'],
                'followers':request.json[7]['followers'],
                'likes':request.json[7]['likes'],
                'posts':request.json[7]['posts'],
            },
        ]).inserted_ids)

        results = []

        for _id in _ids:
            results.append(str(_id))

        return jsonify({'inserted_ids':results})
        

    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count