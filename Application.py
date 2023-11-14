from flask import Flask, render_template, request, redirect, jsonify
from service import StudentService as studentService
from enhance import htmlContentGetService as htmlGetService
import json

app = Flask(__name__)


def init_app():
    print("Initialize the core application.")
    studentService.initDataBaseWhenStartApp()
    return app


if __name__ == '__main__':
    init_app()
    app.run(host='0.0.0.0', port=5000, debug=True)


@app.route('/student/add', methods=['POST'])
def createStudent():
    lastName = request.form['inputLastName']
    firstName = request.form['inputFirstName']
    email = request.form['inputEmail']
    dob = request.form['inputDob']
    address = request.form['inputAddress']
    point = request.form['inputPoint']
    # validate the received values
    isCreateSuccess = studentService.createStudent(lastName, firstName, email, dob, address, point)
    if isCreateSuccess:
        return redirect("/")
    else:
        return "Error"


@app.route('/crawl/')
def getAllStudentInWebContent():
    students = htmlGetService.getStudentHtml()

    with open("store/student.txt", 'a') as f:
        for student in students:
            # vars return __dict__ : https://www.w3schools.com/python/ref_func_vars.asp
            student_data = vars(student)
            # Dạng như kiểu Redis (key,value) nối với nhau bằng dấu ","
            student_line = ', '.join(f"{key}: {value}" for key, value in student_data.items())
            f.write(student_line + '\n')

    return "Export Data Successfully !"


@app.route('/json/<id>')
def getJsonById(id):
    student = studentService.getStudentById(id)
    # Dùng jsonify của Flask để tự động trả về Response và các thuộc tính mặc định như:
    # Content-Type, application/json,v.v.... ( chắc tránh CORS)
    # IMPORTANT : Tự định nghĩa lại to_dict()
    if student is not None:
        return jsonify(student.to_dict())


# Get all student
@app.route('/')
def getAllStudent():
    studentList = studentService.getAllStudent()
    return render_template('index.html', entries=studentList)


@app.route('/create-page')
def loadCreatePage():
    return render_template('add.html')


@app.route('/update-page/<id>')
def loadUpdatePage(id):
    student = studentService.getStudentById(id)
    return render_template('edit.html', student=student)


@app.route('/update', methods=['POST'])
def updateStudent():
    studentNo = request.form['studentNo']
    lastName = request.form['inputLastName']
    firstName = request.form['inputFirstName']
    email = request.form['inputEmail']
    dob = request.form['inputDob']
    address = request.form['inputAddress']
    point = request.form['inputPoint']
    studentService.updateStudent(studentNo, lastName, firstName, email, dob, address, point)
    return redirect("/")


@app.route('/delete/<id>')
def deleteStudent(id):
    studentService.deleteStudent(id)
    return redirect("/")


@app.route('/student/<id>', methods=['GET'])
def getStudentById(id):
    student = studentService.getStudentById(id)
    return json.dumps(vars(student))
