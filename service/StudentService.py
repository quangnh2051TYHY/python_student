from repository import StudentRepository as studentRepository
import sqlite3


def getStudentById(studentId):
    return studentRepository.getStudentById(studentId)


def initDataBaseWhenStartApp():
    connection = sqlite3.connect('database.db')

    with open('flask_student/schema.sql') as f:
        connection.executescript(f.read())
    # Sample
    cur = connection.cursor()
    cur.execute("INSERT INTO students (lastName, firstName, email, dob, address, totalPoint) VALUES (?, ?, ?, ?, ?, ?)",
                ('Ngo', 'Hong Quang', 'quangnh26@fpt.com', '2023-11-07 17:30:22', 'Thach That, Ha Noi', "100")
                )
    connection.commit()
    connection.close()


def createStudent(lastName, firstName, email, dob, address, totalPoint):
    return studentRepository.createStudent(lastName, firstName, email, dob, address, totalPoint)


def getAllStudent():
    return studentRepository.getAllStudent()

def updateStudent(studentNo, lastName, firstName, email, dob, address, totalPoint):
    return studentRepository.updateStudent(studentNo, lastName, firstName, email, dob, address, totalPoint)

def deleteStudent(student_no):
    studentRepository.deleteStudentById(student_no)
