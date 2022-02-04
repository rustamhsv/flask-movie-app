from . import users
from flask import render_template, flash, redirect, url_for, request
from .forms import RegistrationForm, LoginFrom, UpdateAccountForm
from werkzeug.security import generate_password_hash, check_password_hash
from movietracker.models import User
from movietracker import db
from flask_login import current_user, login_required, login_user, logout_user
from .utils import save_picture

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
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('main.home'))
    return render_template('login.html', form=form)


@users.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.photo_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    photo_file = url_for('static', filename='photos/' + current_user.photo_file)
    return render_template('account.html', form=form, photo_file=photo_file)

