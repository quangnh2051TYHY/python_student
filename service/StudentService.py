from python_student.repository import StudentRepository
import sqlite3

def getStudentById(studentId):
    StudentRepository.getStudentById(studentId)

def initDataBaseWhenStartApp():
    connection = sqlite3.connect('database.db')

    with open('flask_student/schema.sql') as f:
        connection.executescript(f.read())
    # Sample
    cur = connection.cursor()

    cur.execute("INSERT INTO students (lastName, firstName, email, dob, address, totalPoint) VALUES (?, ?, ?, ?, ?, ?)",
                ('Ngo', 'Hong Quang', 'quangnh26@fpt.com', '2023-11-07 17:30:22', 'Thach That, Ha Noi', 100)
                )
    connection.commit()
    connection.close()