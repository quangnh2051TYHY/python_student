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

    def to_dict(self):
        return {
            'studentNo': self.studentNo,
            'lastName': self.lastName,
            'firstName': self.firstName,
            'email': self.email,
            'dob': self.dob,
            'address': self.address,
            'totalPoint': self.totalPoint
        }