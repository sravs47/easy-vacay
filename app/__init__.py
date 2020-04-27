import os
import sys

from flask import Flask
from flask import render_template, session, redirect, url_for, flash
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.helpers import utils
from app.helpers.loginHelper import is_logged_in
from app.helpers.registerHelper import RegisterForm
from app.helpers import checkoutHelper
from app.helpers.checkoutHelper import hotel_li_block, flight_li_block
import socket
from flasgger import Swagger


template_folder = (os.path.dirname(sys.modules['__main__'].__file__))
print('********************************' + template_folder)

app = Flask(__name__)
swagger = Swagger(app)
app.config['SECRET_KEY'] = 'SjdnUends821Jsdlkvxh391ksdODnejdDw'

DB_URL = None
try:
    DB_URL = socket.gethostbyname("host.docker.internal")
except socket.gaierror:
    DB_URL = 'localhost'

# config mySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'rootroot'
# app.config['MYSQL_DB'] = 'traveleasy'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:rootroot@{DB_URL}/traveleasy'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.dbModels.flight_listings import flight_listings
from app.dbModels.hotel_listings import hotel_listings
from app.dbModels.order_history import order_history
from app.dbModels.persons import persons
from app.dbModels.promocode import promocode
from app.dbModels.testimonals import testimonals
from app.dbModels.users import users

from app.api import api_routes
from app.routes.blog import blog_routes
from app.routes.register import register_route
from app.routes.login import login_route
from app.routes.pastorders import pastorders_route
from app.routes.checkout import checkout_route
from app.routes.placeorder import placeorder_route

app.register_blueprint(api_routes.api_bp)
app.register_blueprint(blog_routes.blog_bp)
app.register_blueprint(register_route.register_bp)
app.register_blueprint(login_route.login_bp)
app.register_blueprint(pastorders_route.pastorders_bp)
app.register_blueprint(checkout_route.checkout_bp)
app.register_blueprint(placeorder_route.placeorder_bp)


@app.route('/')
def default():
    return render_template('index.html')


@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('index'))


@app.route('/flightStatus')
def flightstatus():
    return render_template('flightStatus.html')


if __name__ == '__main__':
    app.run(debug=True)
