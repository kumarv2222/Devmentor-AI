from flask import Blueprint, jsonify, request, session
from database import db
from model import Student
student_bp = Blueprint("student", __name__)
@student_bp.route('/student', methods=["POST"])
def student():
    data = request.get_json()  # get the JSON data from the request body
    student = Student(name=data['name'], age=data['age'], email=data['email'])
    db.session.add(student)
    db.session.commit()
    return jsonify({
        "message": "Student added successfully",
        
    }),201
    
@student_bp.route('/student',methods=['GET'])
def get_students():
    students= Student.query.all()
    student_list=[]
    for student in students:
        student_list.append({
            "id":student.id,
            "name":student.name,
            "email":student.email,
        })
    return jsonify(student_list)
@student_bp.route('/student/<int:id>',methods=['GET'])
def get_student(id):
    student=Student.query.get(id)
    if student:
        return jsonify({
            "id":student.id,
            "name":student.name,
            "email":student.email,
            
        })
    return jsonify({"message": "Student not found"}), 404
@student_bp.route('/student/<int:id>',methods=['PUT'])
def updated_student(id):
    student=Student.query.get(id)
    if student is None:
        return jsonify({"message":"Student not found"}), 404
    data=request.get_json()
    student.name=data["name"]
    student.age=data["age"]
    student.email=data["email"]
    db.session.commit()
    return jsonify({"message":"Student updated successfully"})
@student_bp.route('/student/<int:id>',methods=['DELETE'])
def delete_student(id):
    student=Student.query.get(id)
    if student is None:
        return jsonify({"message":"Student not found"}),404
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message":"Student deleted successfully"})
    
# if __name__ == "__main__":
#     student_bp.run(debug=True)