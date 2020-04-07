from flask import Blueprint, render_template, request, session, flash, redirect, url_for
from app.helpers.registerHelper import RegisterForm
from app.dbModels.users import users
import datetime
from app import db

register_bp = Blueprint('register_bp', __name__, template_folder='/app/templates')


@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    print(request)
    a = request
    if request.method == 'POST':
        if form.validate():
            result = users(request.form['firstname'], request.form['lastname'], request.form['rusername'],
                           request.form['rpassword'], request.form['email'], datetime.datetime.now())
            db.session.add(result)
            db.session.commit()
            session['logged_in'] = True
            session['username'] = request.form['rusername']
            session['miles'] = 0
            flash('You are now registered and can log in', 'success')
            return redirect(url_for('index'))
        else:
            flash('Verify all the fields properly', 'danger')
    return render_template('register.html')
