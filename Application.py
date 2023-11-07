from flask import Flask
from python_student.service import StudentService as studentService


def init_app():
    print("""Initialize the core application.""")
    app = Flask(__name__)
    studentService.initDataBaseWhenStartApp()
    return app


app = init_app()

# Sample
@app.route('/student/<studentId>')
def getStudentById(studentId):
    studentService.getStudentById(studentId)
    return studentId + ""


# TODO
@app.route('/data/<studentId>', methods=['POST'])
def createStudent(studentId):
    return studentId + ""


# Get all student
@app.route('/')
def getAllStudent():
    return 'Hello, World!'



#TODO
@app.route('/student/<id>', methods=['PUT'])
def updateStudent(id, ):
    return id + ""
