from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flask_wtf.file import FileAllowed, FileField


class RegistrationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm_password = PasswordField('confirm password', validators=[EqualTo('password',
                                                                             message='passwords must match')])
    submit = SubmitField('Register')


class LoginFrom(FlaskForm):
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])

    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('email', validators=[DataRequired(), Email()])
    picture = FileField('update profile picture', validators=[FileAllowed(['jpg', 'png'])])

    submit = SubmitField('Update')

