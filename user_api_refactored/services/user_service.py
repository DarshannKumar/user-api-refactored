from flask import jsonify
from user_api_refactored.models.user_model import *

from utils.validation import validate_user_data, validate_login_data

def get_all_users():
    try:
        users = fetch_all_users()
        return jsonify([dict(u) for u in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_user(user_id):
    try:
        user = fetch_user_by_id(user_id)
        if user:
            return jsonify(dict(user)), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user(request):
    try:
        data = request.get_json()
        print("🔁 Received POST /users with data:", data)

        error = validate_user_data(data)
        if error:
            return jsonify({"error": error}), 400

        insert_user(data['name'], data['email'], data['password'])
        return jsonify({"message": "User created successfully"}), 201
    except Exception as e:
        print("❌ Error in create_user:", str(e))
        return jsonify({"error": str(e)}), 500



def update_user(user_id, request):
    try:
        data = request.get_json()
        if not data.get('name') or not data.get('email'):
            return jsonify({"error": "Name and email are required"}), 400
        
        updated = update_user_by_id(user_id, data['name'], data['email'])
        if updated:
            return jsonify({"message": "User updated"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_user(user_id):
    try:
        deleted = delete_user_by_id(user_id)
        if deleted:
            return jsonify({"message": f"User {user_id} deleted"}), 200
        else:
            return jsonify({"message": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def search_users(name):
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    try:
        users = search_users_by_name(name)
        return jsonify([dict(u) for u in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def login(request):
    try:
        data = request.get_json()
        print("🔁 Received POST /login with data:", data)

        error = validate_login_data(data)
        if error:
            return jsonify({"error": error}), 400

        user = login_user(data['email'], data['password'])
        if user:
            return jsonify({"status": "success", "user_id": user["id"]}), 200
        else:
            return jsonify({"status": "failed"}), 401
    except Exception as e:
        print("❌ Error in login:", str(e))
        return jsonify({"error": str(e)}), 500
