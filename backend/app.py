from flask import Flask,jsonify#//import Flask class from the flask module
app=Flask(__name__)#//create an instance of the Flask class and create a Flask application 
@app.route('/home')#..create a route for the home page of the application
def home():
    return jsonify({
        "author": "kumar",
        "message": "Welcome to DevMentors AI",
        "version": "1.0"
    })
@app.route('/about')#..create a route for the about page of the application
def about():
    return jsonify({
        "description": "This is a sample Flask application that demonstrates how to create a RESTful API using Flask.",
        "language": "python",
        "framework": "Flask",
        "Project": "DevMentors AI"
    })
@app.route('/profile')
def profile():
    return jsonify({
        "name1": "kumar",
        "age": 22,
        "college": "Sahyadri College of Engineering",
        "location": "Mangalore, India",
        "skills": ["python", "sql", "html", "css", "javascript", "flask", "django"]
    })
if __name__ == '__main__':#//check if the script is being run directly (not imported as a module)
    app.run(debug=True)#//start the Flask development server with debug mode enabled