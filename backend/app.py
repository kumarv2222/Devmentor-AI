from flask import Flask
from routes.home import home_bp
from routes.student import student_bp   
from routes.profile import profile_bp
from routes.contact import contact_bp
app=Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(student_bp)
app.register_blueprint(profile_bp)
app.register_blueprint(contact_bp)

if __name__=="__main__":
    app.run(debu=True)