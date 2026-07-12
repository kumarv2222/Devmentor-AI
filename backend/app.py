from flask import Flask#//import Flask class from the flask module
app=Flask(__name__)#//create an instance of the Flask class and create a Flask application 
@app.route('/home')#..create a route for the home page of the application
def home():
    return 'Welcome to DevMentors AI'
@app.route('/about')#..create a route for the about page of the application
def about():
    return 'This is a simple Flask application for DevMentors AI.'
if __name__ == '__main__':
    app.run(debug=True)