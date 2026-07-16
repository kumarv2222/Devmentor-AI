from flask import Flask

from database import db

from routes.home import home_bp
from routes.student import student_bp
from routes.profile import profile_bp
from routes.contact import contact_bp
from routes.auth import auth_bp
from routes.ai import ai_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devmentor.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(home_bp)

app.register_blueprint(student_bp)

app.register_blueprint(profile_bp)

app.register_blueprint(contact_bp)

app.register_blueprint(auth_bp)

app.register_blueprint(ai_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)