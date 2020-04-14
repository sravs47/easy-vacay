from app import db

class hotel_listings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    city = db.Column('city', db.String(20))
    hname = db.Column('hname', db.String(20))
    address = db.Column('address', db.String(50))
    rooms = db.Column('rooms', db.Integer)
    hprice = db.Column('hprice', db.Integer)
    fromdate = db.Column('fromdate', db.Date)
    todate = db.Column('todate', db.Date)
    miles = db.Column('miles', db.Integer)

    def __init__(self, city, hname, address, rooms, hprice, fromdate, todate, miles):
        self.city = city
        self.hname = hname
        self.address = address
        self.rooms = rooms
        self.hprice = hprice
        self.fromdate = fromdate
        self.todate = todate
        self.miles = miles

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
