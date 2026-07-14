from flask import Blueprint, jsonify, request
contact_bp = Blueprint("contact", __name__)
@contact_bp.route('/contact', methods=["POST"])
def contact():
    data = request.get_json()  # get the JSON data from the request body
    return jsonify({
        "message": "Contact information received successfully",
        "contact": data
    })