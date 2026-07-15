from flask import Blueprint, jsonify
profile_bp=Blueprint("profile",__name__)
@profile_bp.route('/profile/<name>/<int:age>')
def profile(name, age):
    return jsonify({
        "name": name,
        "age": age
    })
if __name__=="__main__":
    profile_bp.run(debug=True)