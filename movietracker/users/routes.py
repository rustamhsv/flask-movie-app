from . import users
from flask import render_template, flash, redirect, url_for
from .forms import RegistrationForm


@users.route('/login')
def login():
    return render_template('login.html')


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash('Registration successful', 'success')
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)
