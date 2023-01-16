from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ActivityForm(FlaskForm):
    activity_name = StringField("Create your own Activity", validators=[DataRequired()])
    submit = SubmitField("Create")
