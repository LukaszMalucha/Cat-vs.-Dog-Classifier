from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length, EqualTo


## Login Form

class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80)])
    remember = BooleanField('Remember Me')

## Register Form

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Please enter correct email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, max=80), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')