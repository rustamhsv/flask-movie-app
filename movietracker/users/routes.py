from . import users
from flask import render_template


@users.route('/login')
def login():
    return render_template('login.html')
