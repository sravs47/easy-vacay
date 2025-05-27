# Vacation Planner website to book flights, hotels and packages

## Tools/ Binaries to Install

Install python and pip

(optional, but recommended) Install pyCharm tool. [https://www.jetbrains.com/pycharm/download/#section=mac]

(optional, but recommended) Install virtual environment, https://virtualenvwrapper.readthedocs.io/en/latest/install.html -> For this step, make sure you create the following directory before update the bash file. For MAC Users, its bash_profile in your home directory.

sudo pip3 install virtualenv
virtualenv --version
13.1.2
mkdir $HOME/.virtualenvs
Create virtual environment for your project, say dev1

mkvirtualenv helloflask
Install flask

pip install Flask
Install and set up MySQL Database Flask-MySQLdb==0.2.0 mysqlclient==1.3.13 *You will need to set the environment variable PATH
export PATH=$PATH:/usr/local/mysql/bin You can use MySQL WorkBench for an easy visualized DB access [https://dev.mysql.com/downloads/workbench/]

Install all the below binaries using pip command Flask==1.0.2 Flask-WTF==0.14.2 flask-sqlalchemy Flask-Migrate itsdangerous==0.24 MarkupSafe==1.0 passlib==1.7.1 WTForms==2.2.1 *You can use pyCharm to install the above binaries by creating requirements.txt. It will read from the txt and on confirmation, download the requires binaries.

## Setting up the project

We need to create app.py

from flask import Flask

```
app = Flask(__name__)
@app.route('/')
def index():
     return 'Hello, Flask!'
if __name__ == '__main__':
     app.run(debug=True)
```

Needs git installed and set-up on your machine.
In Terminal, ensure virtual environment is activated, where you want the project,

To activate virtual environment, source bin/activate

```https://github.com/sravs47easy-vacay.git/```

flask db init flask db migrate -m "Initial migration" flask db upgrade

If the above doesnt work, you can also perform:- flask db stamp head flask db migrate flask db upgrade

## To run the project:

To run the app -> Using PyCharm -> Go to app -> init.py file -> right click & run. After that we can open the localhost browser with port 5000 to view our website. http://127.0.0.1:5000/index

## Functionalities

* Account Registration
* Account Login
* Flight Booking
* Hotel Booking
* Package Booking (Flight + Hotel)
* Booking from pre-existing vacation packages
* Accumulate Mileage
* Redeem Mileage
* Flight Status
* Customer Experience Feedback


