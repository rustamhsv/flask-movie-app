from . import users
from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm
from werkzeug.security import generate_password_hash, check_password_hash
from movietracker.models import User
from movietracker import db


@users.route('/login')
def login():
    return render_template('login.html')


@users.route('/register', methods=['GET', 'POST'])
def register():
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
