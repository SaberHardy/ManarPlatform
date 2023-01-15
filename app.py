from models.models import db, StudentModel
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_table():
    db.create_all()


@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('manar/create_student.html')
    if request.method == 'POST':
        # student_id = request.form['student_id']
        fullname = request.form['fullname']
        birthday = request.form['birthday']
        place_of_birth = request.form['place_of_birth']
        inscription_date = request.form['inscription_date']
        sex = request.form['sex']
        group = request.form['group']
        computer_nbr = request.form['computer_nbr']
        parents_phone = request.form['parents_phone']

        student = StudentModel(
            # student_id=student_id,
            fullname=fullname,
            birthday=birthday,
            place_of_birth=place_of_birth,
            inscription_date=inscription_date,
            sex=sex,
            group=group,
            computer_nbr=computer_nbr,
            parents_phone=parents_phone)

        db.session.add(student)
        db.session.commit()

        return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def retrieve_students():
    all_students = StudentModel.query.all()
    return render_template('manar/students.html', all_students=all_students)


if __name__ == '__main__':
    app.run()
