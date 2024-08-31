# models/tuition.py

class Tuition:
    def __init__(self, student, total_tuition_fee):
        self.student = student
        self.total_tuition_fee = total_tuition_fee

    def is_fully_paid(self):
        return self.student.get_total_tuition() >= self.total_tuition_fee

    def get_balance(self):
        return self.total_tuition_fee - self.student.get_total_tuition()