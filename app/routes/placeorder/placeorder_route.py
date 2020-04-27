
from flask import Blueprint, render_template, request, session
from app.dbModels.flight_listings import flight_listings
from app.dbModels.order_history import order_history
from app.dbModels.hotel_listings import hotel_listings
from app.dbModels.users import users
from app import db
import datetime

placeorder_bp = Blueprint('placeorder_bp', __name__, template_folder='/app/templates')

@placeorder_bp.route('/order', methods=['POST', 'GET'])
def placeOrder():
    if request.method == 'POST':
        # form = request.form
        order: order_history = order_history.query.filter_by(username=session['username'],
                                                             order_status='incomplete').order_by(
            order_history.id.desc()).first()
        order.email = request.form['email']
        order.address = request.form['address'] + request.form['address2'] + request.form['country'] + request.form[
            'state'] + request.form['zip']
        order.total_price = int(request.form['Amount'][1:])
        order.card_name = request.form.get('cc-name', None)
        order.card_type = request.form.get('paymentMethod', None)
        order.card_number = request.form.get('cc-number', None)
        order.cvv_no = request.form.get('cc-cvv', None)
        order.order_status = 'complete'
        order.purchase_date = datetime.datetime.now()

        user: users = users.query.filter_by(username=order.username).first()

        if order.card_number is not None and order.card_number == '' and user.miles < 25000:
            return render_template('ordersummaryerror.html', miles=user.miles)

        if order.flight_id is not None:
            flightlisting: flight_listings = flight_listings.query.filter_by(id=order.flight_id).first()

            if order.card_number is None and order.card_number == '' and flightlisting.type == 'International' and user.miles < 50000:
                return render_template('ordersummaryerror.html', miles=user.miles)
            flightlisting.seatcount = flightlisting.seatcount - order.total_persons
            user.miles = user.miles + flightlisting.miles

        if order.hotel_id is not None:
            hotellisting: hotel_listings = hotel_listings.query.filter_by(id=order.hotel_id).first()
            hotellisting.rooms = hotellisting.rooms - 1

        db.session.commit()

        if order.card_number is not None and order.card_number == '':
            user.miles = user.miles - 25000 if flightlisting.type == 'Domestic' else user.miles - 50000
            session['miles'] = user.miles

        db.session.commit()
        return render_template('ordersummary.html', orderid=order.id)
    return render_template('index.html')

