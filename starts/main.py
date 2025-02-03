from flask import Flask,render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField


class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_adress= StringField(label='email address')
    password1 = PasswordField(label='password1')
    password1 = PasswordField(label='password2')
    submit=SubmitField(label='submit')
    

 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jawad'  
 
@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')


@app.route('/Art')
def Artpage():
    return render_template('Art.html')

@app.route('/Data')
def Datapage():
    return render_template('Data.html')

@app.route('/Image')
def Imagepage():
    return render_template('Image.html')

@app.route('/Audio')
def Audiopage():
    return render_template('Audio.html')

@app.route('/register')
def registerpage():
    form=RegisterForm()
    return render_template('register.html',form=form)
    






if __name__ == "__main__":
    app.run(debug=True)