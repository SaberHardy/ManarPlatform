import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import expression

db = SQLAlchemy()

Base = declarative_base()


# class ActivityType(Base):
#     SCHOOLS = [
#         ('Programming Club', 'Programming Club'),
#         ('Robotics', 'Robotics'),
#         ('The Digital Library', 'The Digital Library'),
#         ('The Digital Picture', 'The Digital Picture'),
#         ('Graphic Club', 'Graphic Club'),
#     ]


class ActivityType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    activity_name = db.Column(db.String(255))

    def __repr__(self):
        return f"{self.activity_name}"


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

    education_level = db.Column(db.String())
    # membership = db.Column(db.String())

    activity_type = db.Column(db.String())
    # activity_type = sqlalchemy_utils.types.choice.ChoiceType(ActivityType)

    # photo = FileField("photo", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    # TODO: This is a checkbox
    # paid = db.Column(db.Boolean())

    def __init__(self, fullname, birthday, place_of_birth,
                 inscription_date, sex, group, education_level, computer_nbr,
                 parents_phone, activity_type):
        # self.student_id = student_id
        self.fullname = fullname
        self.birthday = birthday
        self.place_of_birth = place_of_birth
        self.inscription_date = inscription_date
        self.sex = sex
        self.group = group
        self.education_level = education_level
        self.computer_nbr = computer_nbr
        self.parents_phone = parents_phone
        self.activity_type = activity_type

    def __repr__(self):
        return f"{self.fullname}"

    def calculate_age(self):
        pass
