from flask import Flask
from database import db
from routes.home import home_bp
from routes.student import student_bp   
from routes.profile import profile_bp
from routes.contact import contact_bp
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devmentor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.register_blueprint(home_bp)
app.register_blueprint(student_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(contact_bp)

if __name__=="__main__":
    with app.app_context():
        db.create_all()  # Create the database tables if they don't exist
    app.run(debug=True)