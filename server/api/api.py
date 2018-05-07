
from flask_restful import Api, Resource, reqparse
from flask import Blueprint, jsonify, Response, current_app
from server import models, bcrypt
import json
import os

api_blueprint = Blueprint('api', __name__,)
api = Api(api_blueprint )



class Documentation(Resource):
    """
    Represents the documentation page of the API
    """
    def get(self):
        return {
            'test': '/api/v1.0/test'
        }

class User(Resource):
    """
    Represents the API data dump from the common schema database
    """
    #TODO: Account for other filetypes/Cache data tables

    def get(self, user_id):

        # Processing

        return json_user

##Function private 
class Authenticate(Resource):

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str)
        parser.add_argument('password_hash', type=str)

        user = models.User.objects.get(username=parser.parse_args()['username'])
        print(bcrypt.check_password_hash(user.password, parser.parse_args()['password']))
        if user and bcrypt.check_password_hash(user.password, parser.parse_args()['password']):
            return jsonify({'username': user.username, 'address':user.address, 'authenticated':True, 'registered_on':user.registered_on})
        else:
            return 'AUTHENTICATION ERROR'


api.add_resource(Documentation, '/api')
api.add_resource(User, '/api/<user_id>')
api.add_resource(Authenticate, '/api/authenticate')
