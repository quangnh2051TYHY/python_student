from flask import Flask, render_template, request, redirect
from python_student.service import StudentService as studentService
from python_student.enhance import htmlContentGetService as htmlGetService
import json


def init_app():
    print("""Initialize the core application.""")
    app = Flask(__name__)
    studentService.initDataBaseWhenStartApp()
    return app


app = init_app()


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
    f = open("store/student.txt", 'a')
    # Jump to end of file to write append
    f.seek(0, 2)
    jsonStudentList = []
    for student in students:
        jsonStudentList.append(json.dumps(vars(student)))
        f.write(str(vars(student)))
        f.write('\n')

    f.close()
    return jsonStudentList


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
