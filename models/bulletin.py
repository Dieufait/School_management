# models/bulletin.py

class Bulletin:
    def __init__(self, student):
        self.student = student

    def generate_report(self):
        report = f"Bulletin de {self.student.name} (ID: {self.student.student_id})\\n"
        report += "-------------------------------\\n"
        for course, grade in self.student.courses.items():
            report += f"{course}: {grade}\\n"
        report += f"Moyenne générale: {self.student.get_average_grade()}\\n"
        return report