from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username =StringField('Username',
                          validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                           validators=[DataRequired(), Email(), Length(min=2, max=60)])
    password = PasswordField('Password',
                           validators=[DataRequired()])
    confirmPassword = PasswordField('Password',
                           validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is taken. Please choose a different one')



class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email(), Length(min=2, max=60)])
    password = PasswordField('Password',
                             validators=[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Log in')
