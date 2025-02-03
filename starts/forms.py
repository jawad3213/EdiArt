from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitButton



class RegisterForm(FlaskForm):
    username = StringField(label='username')
    email_address= StringField(label='email address')
    password1 = PasswordField(label='password1')
    password1 = PasswordField(label='password2')
    submit=SubmitButton(label='submit')
    