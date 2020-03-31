import os
import sys

from flask import Flask
from flask import render_template, session, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func
from jinja2 import Markup


template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************' + template_folder)

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(debug=True)
