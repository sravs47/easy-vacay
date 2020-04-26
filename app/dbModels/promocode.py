from app import db

class promocode(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    promo_code = db.Column('promo_code', db.String(10))
    discount_percentage = db.Column('discount_percentage', db.Integer)

    def __init__(self, promo_code, discount_percentage):
        self.promo_code = promo_code
        self.discount_percentage = discount_percentage
