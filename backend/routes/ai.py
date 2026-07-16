from flask import Blueprint, request, jsonify

ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/explain", methods=["POST"])
def explain_code():
    data = request.get_json()
    code = data.get("code") if data else None

    if not code:
        return jsonify({"message": "Code is required"}), 400

    explanation = [
        "This is a placeholder explanation.",
        "The AI integration will be added on Day 12.",
        "Your submitted code was received successfully.",
    ]
    return jsonify({
        "language": "python",
        "line":len(code.splitlines()),
        "code": code, 
        "explanation": explanation}), 200
