# models/student.py

class Student:
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.courses = {}
        self.tuition_paid = 0

    def add_course(self, course_name, grade):
        self.courses[course_name] = grade

    def get_average_grade(self):
        if not self.courses:
            return 0
        return sum(self.courses.values()) / len(self.courses)

    def add_tuition_payment(self, amount):
        self.tuition_paid += amount

    def get_total_tuition(self):
        return self.tuition_paid