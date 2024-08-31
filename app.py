from flask import Flask, request, render_template, redirect, url_for
from models.student import Student
from models.bulletin import Bulletin
from models.tuition import Tuition

app = Flask(__name__)

# Simuler une base de données en mémoire
students = {}

@app.route('/')
def index():
    return render_template('index.html', students=students.values())

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form['student_id']
    name = request.form['name']
    email = request.form['email']
    students[student_id] = Student(student_id, name, email)
    return redirect(url_for('index'))

@app.route('/add_course/<student_id>', methods=['POST'])
def add_course(student_id):
    course_name = request.form['course_name']
    grade = float(request.form['grade'])
    student = students.get(student_id)
    if student:
        student.add_course(course_name, grade)
    return redirect(url_for('view_student', student_id=student_id))

@app.route('/view_student/<student_id>')
def view_student(student_id):
    student = students.get(student_id)
    if student:
        bulletin = Bulletin(student)
        tuition = Tuition(student, 1000)  # Ex: Frais de scolarité total de 1000
        return render_template('student.html', student=student, bulletin=bulletin, tuition=tuition)
    return "Student not found", 404

@app.route('/pay_tuition/<student_id>', methods=['POST'])
def pay_tuition(student_id):
    amount = float(request.form['amount'])
    student = students.get(student_id)
    if student:
        student.add_tuition_payment(amount)
    return redirect(url_for('view_student', student_id=student_id))

if __name__ == "__main__":
    app.run(host='0.0.0', debug=True)
