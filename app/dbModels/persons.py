from app import db
from sqlalchemy import ForeignKey

class persons(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    user_id = db.Column('user_id', db.Integer, ForeignKey("users.id"))
    first_name = db.Column('first_name', db.String(30))
    last_name = db.Column('last_name', db.String(30))

    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
