import os
import sys

from flask import Flask
from flask import render_template, session, request, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, func
from jinja2 import Markup
from app.helpers.registerHelper import RegisterForm
from app.dbModels.users import users
import datetime

template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************' + template_folder)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

# config mySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'rootroot'
app.config['MYSQL_DB'] = 'traveleasy'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:rootroot@localhost/traveleasy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app.routes.register import register_route
app.register_blueprint(register_route.register_bp)


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
