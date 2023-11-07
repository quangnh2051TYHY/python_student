DROP TABLE IF EXISTS students;
CREATE TABLE students (
    studentNo INTEGER PRIMARY KEY AUTOINCREMENT,
    lastName TEXT,
    firstName TEXT,
    email TEXT,
    dob TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    address TEXT,
    totalPoint TEXT
);