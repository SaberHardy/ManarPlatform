from secret_key import MY_SECRET_KEY
from models.models import db, StudentModel
from django.shortcuts import get_object_or_404
from flask_migrate import Migrate

from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)
migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = MY_SECRET_KEY
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
        activity_type = request.form['activity_type']
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
            activity_type=activity_type,
            computer_nbr=computer_nbr,
            parents_phone=parents_phone)

        db.session.add(student)
        db.session.commit()

        return redirect('/')


@app.route('/', methods=['GET', 'POST'])
def retrieve_students():
    all_students = StudentModel.query.all()
    return render_template('manar/students.html', all_students=all_students)


@app.route('/single/<int:id>')
def single_student(id):
    # student = StudentModel.query.filter_by(id=id).first()
    student = StudentModel.query.get_or_404(id)

    return render_template('manar/single.html', student=student)


@app.route('/<int:id>/update', methods=['GET', 'POST'])
def update_student(id):
    student_to_update = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if student_to_update:
            db.session.delete(student_to_update)
            db.session.commit()

            fullname = request.form['fullname']
            birthday = request.form['birthday']
            place_of_birth = request.form['place_of_birth']
            inscription_date = request.form['inscription_date']
            sex = request.form['sex']
            group = request.form['group']
            activity_type = request.form['activity_type']
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
                activity_type=activity_type,
                computer_nbr=computer_nbr,
                parents_phone=parents_phone)
            db.session.add(student)
            db.session.commit()

            return redirect(f'/')
        return f"The student cant be updated"
    return render_template('manar/update_student.html', student_to_update=student_to_update)


@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    student_to_delete = StudentModel.query.get_or_404(id)
    try:
        StudentModel.query.get_or_404(id)
        db.session.delete(student_to_delete)
        db.session.commit()

        # Return a message
        flash("Blog Post Was Deleted!")

        # Grab all the posts from the database
        students = StudentModel.query.order_by(StudentModel.date_posted)
        return render_template("manar/students.html", all_students=students)
    except:
        flash("The student doesnt exist")
        return redirect(url_for('retrieve_students'))


if __name__ == '__main__':
    app.run()
