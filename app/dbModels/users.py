from app import db

class users(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    firstname = db.Column('firstname', db.String(20))
    lastname = db.Column('lastname', db.String(20))
    username = db.Column('username', db.String(30), unique=True)
    password = db.Column('password', db.String(100))
    email = db.Column('email', db.String(100))
    register_date = db.Column('register_date', db.DateTime)
    miles = db.Column('miles', db.Integer, nullable=True)
    phoneno = db.Column('phoneno', db.String(20), nullable=True)

    def __init__(self, firstname, lastname, username, password, email, register_date, miles=0, phoneno=None):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.email = email
        self.register_date = register_date
        self.miles = miles
        self.phoneno = phoneno

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
