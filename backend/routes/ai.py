from flask import Blueprint, request, jsonify
from services.ai_services import explain_python_code
ai_bp = Blueprint("ai", __name__)


@ai_bp.route("/explain", methods=["POST"])
def explain_code():
    data = request.get_json()
    code = data.get("code") if data else None

    if not code:
        return jsonify({"message": "Code is required"}), 400

    explanation = explain_python_code(code)
    return jsonify({
        "language": "python",
        "line":len(code.splitlines()),
        "code": code, 
        "explanation": explanation}), 200
