from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.dbModels.users import users

login_bp = Blueprint('login_bp', __name__, template_folder='/app/templates')

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_candidate = request.form['password']
        user: users = users.query.filter_by(username=username, password=password_candidate).first()
        if user is not None:
            session['logged_in'] = True
            session['username'] = username
            session['miles'] = user.miles
            flash('You are now logged in', 'success')
            return redirect(url_for('index'))
        else:
            error = 'Invalid login'
            return render_template('register.html', error=error)
    else:
        error = 'Username not found'
        return render_template('register.html', error)
    return render_template('register.html')
