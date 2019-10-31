from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,FileField,validators  #....
from wtforms.validators import DataRequired,Email,Length,regexp

app = Flask(__name__)


name=['Andrea','Elena','Edoardo','Francesco']
app.config['SECRET_KEY']='kjdvkjfbvksfbvkdfbvkfhbvkdfbvkdjfbvd.fkjbv.dfkjbv'

# name=['Andera']

class userForm(FlaskForm):
    name=StringField('Name',validators=[DataRequired(),Length(min=2,max=20)])
    surename=StringField('Surename',validators=[DataRequired(),Length(min=2,max=20)])
    email=StringField('Email',validators=[DataRequired(),Length(min=2,max=30),Email()])
    submit=SubmitField('Submit')


@app.route('/form',methods=['POST','GET'])
def formpage():
    name=None # ''
    nameform=userForm()
    if nameform.validate_on_submit():
        name=nameform.name.data
        surename=nameform.surename.data
        email=nameform.email.data
        return render_template('form.html',name=name,sure=surename,email=email,nameform=nameform)
    return render_template('form.html', name=name, nameform=nameform)


@app.route('/studenthtml/<int:id>')
def userhtm(id):
    return render_template('student.html',name=name[id])

@app.route('/home')
def home():
    return render_template('main.html' , Pagename='Home page')




@app.route('/user')
def userpage():
    return render_template('user.html' , Pagename='Home page')


@app.route('/')
def hello_world():
    return 'Hello World!'

# comment in windows and linux is contr+/
# Mac command + /
@app.route('/student/<int:id>')
def user(id):
    return 'Hello World! %s' % name[id]









if __name__ == '__main__':
    app.run()
