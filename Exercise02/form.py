from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,validators,SubmitField,ValidationError
from wtforms.validators import DataRequired,Length
from app import User



class registerationForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired()])
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=20)])
    submit=SubmitField('Register')

    ## Exercise 04
    def validate_username(self,username):
        user=User.query.filter_by(username=self.username.data).first()
        if user:
            raise ValidationError('"%s" is exist, please select new username' % username.data)


    # def validate_username(self,username):





class loginForm(FlaskForm):
    username=StringField('Username',validators=[DataRequired()])
    password=PasswordField('Password',validators=[DataRequired(),Length(min=4,max=20)])
    submit=SubmitField('Register')
