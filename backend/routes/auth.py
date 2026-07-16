from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from database import db
from model import User

auth_bp = Blueprint("auth", __name__)


# ---------------- Register ----------------

@auth_bp.route("/register", methods=["POST"])
def register():

    data = request.get_json()

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({
            "message": "All fields are required"
        }), 400

    existing_user = User.query.filter_by(email=email).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists"
        }), 409

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User registered successfully"
    }), 201


# ---------------- Login ----------------

@auth_bp.route("/login", methods=["POST"])
def login():

    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()

    if user is None:
        return jsonify({
            "message": "User not found"
        }), 404

    if check_password_hash(user.password, password):

        return jsonify({
            "message": "Login successful"
        }), 200

    return jsonify({
        "message": "Invalid password"
    }), 401