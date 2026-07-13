from flask import Flask,jsonify,request#//import Flask class from the flask module
app=Flask(__name__)#//create an instance of the Flask class and create a Flask application 
@app.route('/home')#..create a route for the home page of the application
def home():
    #return "Dev mentor"  // plain text response
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
@app.route('/contact')
def contact():
    return jsonify({
    "email":"your-email@example.com",
    "github":"your-github-link",
    "linkedin":"your-linkedin-link"
})
@app.route('/student', methods=["POST"])
def student():
    data = request.get_json()  # get the JSON data from the request body
    return jsonify({
        "message": "Student added successfully",
        "student": data
})
@app.route('/feedback', methods=["POST"])
def feeback():
    info=request.get_json()
    return jsonify({
        "message": "Your feedback has been received successfully",
        "feedback": info
    })
if __name__ == '__main__':  # check if the script is being run directly (not imported as a module)
    app.run(debug=True)  # start the Flask development server with debug mode enabled