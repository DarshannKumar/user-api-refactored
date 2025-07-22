from flask import Blueprint, request, jsonify
from user_api_refactored.services.user_service import *


user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/')
def home():
    return jsonify({"message": "User Management System"}), 200

@user_routes.route('/users', methods=['GET'])
def get_all_users_route():
    return get_all_users()

@user_routes.route('/user/<user_id>', methods=['GET'])
def get_user_route(user_id):
    return get_user(user_id)

@user_routes.route('/users', methods=['POST'])
def create_user_route():
    return create_user(request)

@user_routes.route('/user/<user_id>', methods=['PUT'])
def update_user_route(user_id):
    return update_user(user_id, request)

@user_routes.route('/user/<user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    return delete_user(user_id)

@user_routes.route('/search', methods=['GET'])
def search_users_route():
    name = request.args.get('name')
    return search_users(name)

@user_routes.route('/login', methods=['POST'])
def login_route():
    return login(request)
