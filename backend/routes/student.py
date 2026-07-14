from flask import Blueprint, jsonify, request
student_bp = Blueprint("student", __name__)
@student_bp.route('/student', methods=["POST"])
def student():
    data = request.get_json()  # get the JSON data from the request body
    return jsonify({
        "message": "Student added successfully",
        "student": data
    })
if __name__ == "__main__":
    student_bp.run(debug=True)