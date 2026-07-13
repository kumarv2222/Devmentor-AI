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
@app.route('/profile/<name>/<int:age>')
def profile(name, age):
    return jsonify({
        "name": name,
        "age": age,
        "college": "Sahyadri College of Engineering",
        "location": "Mangalore, India",
        "skills": ["python", "sql", "html", "css", "javascript", "flask", "django"]
    })
@app.route('/square/<int:number>')
def square(number):
    return jsonify({
        "number": number,
        "square": number ** 2
        
        
    })
@app.route('/cube/<int:num>')
def cube(num):
    return jsonify({
        "number":num,
        "cube":num**3
    })
@app.route('/greet/<name>')
def greet(name):
    return jsonify({
        "message":f"hello,{name}!"
    })

@app.route('/sub')
def sub():
    course=request.args.get('course')
    return jsonify({
        "course": course
    })
@app.route('/calc')
def calc():
    num1=request.args.get('num1',type=int)
    num2=request.args.get('num2',type=int)
    return jsonify({
        'sum':num1+num2
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