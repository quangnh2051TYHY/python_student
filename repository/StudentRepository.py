import sqlite3





def createStudent():
    connection = sqlite3.connect('database.db')

    connection.close()


# TODO
def getAllStudent():
    connection = sqlite3.connect('database.db')
    # Todo thay table
    cursor = connection.execute("SELECT * FROM students")
    for row in cursor:
        print(row)
    connection.close()


# TODO
def getStudentById(studentId):
    connection = sqlite3.connect('database.db')

    cursor = connection.execute("SELECT * FROM students where studentNo = ?", studentId)
    for row in cursor:
        print(row)
    connection.close()


# TODO
def updateStudent(id, lastName, firstName, email, dob, address, totalPoint):
    connection = sqlite3.connect('database.db')

    connection.close()


# TODO
def deleteStudentById():
    connection = sqlite3.connect('database.db')

    connection.close()
