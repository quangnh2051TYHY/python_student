class Student:
    studentNo = 0
    lastName = ''
    firstName = ''
    email = ''
    dob = ''
    address = ''
    totalPoint = 0

    def __init__(self, studentNo, lastName, firstName, email, dob, address, totalPoint):
        self.studentNo = studentNo
        self.lastName = lastName
        self.firstName = firstName
        self.email = email
        self.dob = dob
        self.address = address
        self.totalPoint = totalPoint