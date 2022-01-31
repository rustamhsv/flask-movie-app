from . import users
from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm, LoginFrom
from werkzeug.security import generate_password_hash, check_password_hash
from movietracker.models import User
from movietracker import db
from flask_login import current_user, login_required


@users.route('/register', methods=['GET', 'POST'])
def register():
    # if user already signed in then redirect user to home page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)

        # add users to database session
        db.session.add(user)

        # commit users
        db.session.commit()

        flash('Registration successful', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    # if user already signed in then redirect user to home page
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginFrom()
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    return "<h1>ACCOUNT</h1>"

