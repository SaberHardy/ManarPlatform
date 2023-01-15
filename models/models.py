from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class StudentModel(db.Model):
    __tablename__ = 'table'

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer(), unique=True)
    fullname = db.Column(db.String())
    birthday = db.Column(db.String())
    place_of_birth = db.Column(db.String())
    inscription_date = db.Column(db.String())
    sex = db.Column(db.String())
    group = db.Column(db.String())
    computer_nbr = db.Column(db.Integer)
    parents_phone = db.Column(db.Integer)

    """These three fields should be a relationship"""

    # education_level = db.Column(db.String())
    # membership = db.Column(db.String())
    # activity_type = db.Column(db.String())
    # photo = FileField("photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    # TODO: This is a checkbox
    # paid = db.Column(db.Boolean())

    def __init__(self, fullname, birthday, place_of_birth,
                 inscription_date, sex, group, computer_nbr, parents_phone):
        # self.student_id = student_id
        self.fullname = fullname
        self.birthday = birthday
        self.place_of_birth = place_of_birth
        self.inscription_date = inscription_date
        self.sex = sex
        self.group = group
        self.computer_nbr = computer_nbr
        self.parents_phone = parents_phone

    def __repr__(self):
        return f"{self.fullname}"

    def calculate_age(self):
        pass
