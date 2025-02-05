from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField



class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address= StringField(label='Email address')
    password1 = PasswordField(label='Password')
    password2 = PasswordField(label='Confirm the Password')
    submit=SubmitField(label='submit')
    