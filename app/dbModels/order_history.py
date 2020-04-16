from app import db
from sqlalchemy import ForeignKey
import datetime

class order_history(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(30), ForeignKey("users.username"))
    ordernumber = db.Column('ordernumber', db.String(30), nullable=True)
    card_type = db.Column('card_type', db.String(10), nullable=True)
    card_number = db.Column('card_number', db.String(20), nullable=True)
    cvv_no = db.Column('cvv_no', db.String(3), nullable=True)
    card_name = db.Column('card_name', db.String(30), nullable=True)
    flight_id = db.Column('flight_id', db.Integer, ForeignKey("flight_listings.id"), nullable=True)
    hotel_id = db.Column('hotel_id', db.Integer, ForeignKey("hotel_listings.id"), nullable=True)
    total_persons = db.Column('total_persons', db.Integer, nullable=True)
    total_price = db.Column('total_price', db.Integer, nullable=True)
    order_status = db.Column('order_status', db.String(15))
    email = db.Column('email', db.String(30), nullable=True)
    address = db.Column('address', db.String(50), nullable=True)
    purchase_date = db.Column('purchase_date', db.Date)

    def __init__(self, username, order_status, card_type=None, cvv_no=None, card_name=None, total_persons=None,
                 total_price=None, email=None, address=None, flight_id=None, hotel_id=None, ordernumber=None,
                 purchase_date=datetime.date.today()):
        self.username = username
        self.ordernumber = ordernumber
        self.card_type = card_type
        self.cvv_no = cvv_no
        self.card_name = card_name
        self.total_persons = total_persons
        self.total_price = total_price
        self.flight_id = flight_id
        self.hotel_id = hotel_id
        self.order_status = order_status
        self.email = email
        self.address = address
        self.purchase_date = purchase_date
