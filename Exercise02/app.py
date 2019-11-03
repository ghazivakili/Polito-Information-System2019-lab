from flask import Flask,render_template,redirect,session
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt



app = Flask(__name__)



app.config['SECRET_KEY']='ldjashfjahef;jhasef;jhase;jfhae;'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///website.db'
Bootstrap(app)
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)

## Exercise 01
class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),nullable=True)
    username=db.Column(db.String(64),index=True,unique=True)
    password=db.Column(db.String(128),nullable=False)
    role_id=db.Column(db.Integer,db.ForeignKey('role.id'))

    def __repr__(self):
        return '<User %s>'% self.username


class Role(db.Model):
    __tablename__='role'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(64),index=True)
    users=db.relationship('User',backref='role')

    def __repr__(self):
        return '<Role %s>'% self.name

from form import registerationForm,loginForm

## Exercise 02
@app.before_first_request
def create_all():
    db.create_all()
    db.session.add(Role(name='Student'))
    db.session.add(Role(name='Teacher'))
    db.session.commit()


@app.route('/')
@app.route('/home')
@app.route('/index')
@app.route('/main')
def home():
    return render_template('layout.html')


## Exercise 03
@app.route('/register',methods=['POST','GET'])
def register():
    formRed=registerationForm()
    if formRed.validate_on_submit():
        role=Role.query.filter_by(name='Student').first()
        password_1=bcrypt.generate_password_hash(formRed.password.data)
        new_user=User(name=formRed.name.data,username=formRed.username.data,password=password_1,role_id=role.id)
        db.session.add(new_user)
        db.session.commit()
        return redirect('login')
    return render_template('register.html',formReg=formRed)

## Exercise 05
@app.route('/login',methods=['POST','GET'])
def login():
    if session.get('username'):
        return redirect('profile')
    else:
        formRed = loginForm()
        if formRed.validate_on_submit():
            user_selected=User.query.filter_by(username=formRed.username.data).first()
            if bcrypt.check_password_hash(user_selected.password,formRed.password.data):
                session['username']=user_selected.username
                return redirect('home')
        return render_template('login.html',formReg=formRed)


@app.route('/profile')
def profile():
    return render_template('profile.html')

if __name__ == '__main__':
    app.run()
