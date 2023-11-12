import sqlite3
from model import Student as student


def createStudent(lastName, firstName, email, dob, address, totalPoint):
    try:
        connection = sqlite3.connect('database.db')
        sql = "INSERT INTO students(lastName, firstName, email, dob, address, totalPoint) VALUES (?, ?, ?, ?, ?, ?)"
        data = (lastName, firstName, email, dob, address, totalPoint)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
        return True
    except Exception as ex:
        print(ex)
        return False
    finally:
        cursor.close()
        connection.close()


def getAllStudent():
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.execute("SELECT * FROM students")
        studentList = []
        for row in cursor:
            studentNo = row[0]
            lastName = row[1]
            firstName = row[2]
            email = row[3]
            dob = row[4]
            address = row[5]
            point = row[6]
            studentList.append(student.Student(studentNo, lastName, firstName, email, dob, address, point))

        return studentList
    finally:
        cursor.close()
        connection.close()



def getStudentById(studentId):
    try:
        connection = sqlite3.connect('database.db')

        cursor = connection.execute("SELECT * FROM students where studentNo = ?", studentId)
        for row in cursor:
            studentNo = row[0]
            lastName = row[1]
            firstName = row[2]
            email = row[3]
            dob = row[4]
            address = row[5]
            point = row[6]
            return student.Student(studentNo, lastName, firstName, email, dob, address, point)

    finally:
        cursor.close()
        connection.close()


def updateStudent(studentNo, lastName, firstName, email, dob, address, totalPoint):
    try:
        connection = sqlite3.connect('database.db')
        sql = ("UPDATE students SET lastName = ?, firstName = ?, email = ?, dob = ?, "
               "address = ?, totalPoint = ? WHERE studentNo = ?")
        data = (lastName, firstName, email, dob, address, totalPoint,
                studentNo)
        cursor = connection.cursor()
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()


def deleteStudentById(studentNo):
    try:
        connection = sqlite3.connect('database.db')
        cursor = connection.execute("DELETE FROM students WHERE studentNo = ?", studentNo)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
