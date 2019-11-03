from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,validators
from wtforms.validators import DataRequired,Email,Length


class nameForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=1,max=20)])
    surename=StringField('Surename',validators=[DataRequired(),Length(min=1,max=20)])
    submit=SubmitField('Submit')