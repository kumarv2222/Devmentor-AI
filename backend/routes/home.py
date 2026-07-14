from flask import Blueprint,jsonify

home_bp=Blueprint("home",__name__)
@home_bp.route('/')#..create a route for the home page of the application
def home():
    return jsonify({
        "name":"Kumar",
        "message":"Welcome to DevMentors AI",
    })
@home_bp.route('/about')
def about():
    return jsonify({
        "description": "This is a sample Flask application that demonstrates how to create a RESTful API using Flask.",
        "language": "python",
        "framework": "Flask",
        "Project": "DevMentors AI"
    })
if __name__=="__main__":
    home_bp.run(debug=True)