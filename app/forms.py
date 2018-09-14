from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    email = StringField('Email (phone for mobile accounts)', validators=[DataRequired()])

    submit = SubmitField('Continue')


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me signed in.')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()], render_kw={
                             "placeholder": "At least 6 characters"})
    password1 = PasswordField(
        'Re-enter Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Create your Company account')

    # no need to call, system knows that 'validate_' needs to be run
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Email already taken.')
