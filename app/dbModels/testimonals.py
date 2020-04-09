from app import db
from sqlalchemy import ForeignKey, func

class testimonals(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30), ForeignKey("users.username"))
    comment = db.Column('comment', db.String(250))
    rating = db.Column('rating', db.Integer)
    c_date = db.Column('c_date', db.DateTime, default=func.sysdate())

    def __init__(self, username, comment, rating, c_date):
        self.username = username
        self.comment = comment
        self.rating = rating
        self.c_date = c_date

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
