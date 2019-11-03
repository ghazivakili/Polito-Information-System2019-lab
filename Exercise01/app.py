from flask import Flask
from flask import render_template,redirect,url_for
from forms import nameForm
app = Flask(__name__)
app.config["SECRET_KEY"]="ksdhclascasbcabslab"

names=["Andrea","Elena","Edoardo","Francesco"]



@app.route('/')
def hello_world():
    return 'Hello World!'
#Exercise 1
@app.route('/name/<int:id>')
def name(id):
    return 'Hello %s!' % names[id]

#Exercise 2
@app.route('/namehtml/<int:id>')
def namehtml(id):
    return render_template('index.html',name=names[id])

#Exercise 3
@app.route('/namehtmlcss/<int:id>')
def namehtmlcss(id):
    return render_template('index-css.html',name=names[id])



#Exercise 4
@app.route('/form',methods=["POST","GET"])
def nameformtest():
    forms=nameForm()
    name=[]
    name.insert(2, False)
    if forms.is_submitted():
        name.insert(0,forms.name.data)
        name.insert(1,forms.surename.data)
        name.insert(2,True)
        return render_template('index-form.html',forms=forms,name=name)
    return render_template('index-form.html',forms=forms,name=name)



if __name__ == '__main__':
    app.run()
