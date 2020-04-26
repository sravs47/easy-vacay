from app import db

class flight_listings(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    airlines = db.Column('airlines', db.String(20))
    flight_no = db.Column('flight_no', db.String(10))
    source = db.Column('source', db.String(20))
    destination = db.Column('destination', db.String(20))
    starttime = db.Column('starttime', db.Date)
    endtime = db.Column('endtime', db.Date)
    seatcount = db.Column('seatcount', db.Integer)
    amount = db.Column('amount', db.Integer)
    miles = db.Column('miles', db.Integer)
    status = db.Column('status', db.String(10))
    type = db.Column('type', db.String(30))
    begins = db.Column('begins', db.String(5))
    ends = db.Column('ends', db.String(5))
    notes = db.Column('notes', db.String(100))

    def __init__(self, airlines, flight_no, source, destination, starttime, endtime, seatcount, amount, miles, status,
                 type, begins, ends, notes = None):
        self.airlines = airlines
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.starttime = starttime
        self.endtime = endtime
        self.seatcount = seatcount
        self.amount = amount
        self.miles = miles
        self.status = status
        self.type = type
        self.begins = begins
        self.ends = ends
        self.notes = notes

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
