from flask import Blueprint, render_template, session
from app.dbModels.flight_listings import flight_listings
from app.dbModels.order_history import order_history
from app.dbModels.hotel_listings import hotel_listings
from app.helpers.loginHelper import is_logged_in
from jinja2 import Markup

pastorders_bp = Blueprint('pastorders_bp', __name__, template_folder='app/templates')

@pastorders_bp.route('/pastorders')
@is_logged_in
def pastorders():
    orderblock = ''
    flight_ids = {}
    hotel_ids = {}
    orders: order_history = order_history.query.filter_by(username=session['username'], order_status='complete')
    for order in orders:
        flight: flight_listings = flight_listings.query.filter_by(id=order.flight_id).first()
        hotel: hotel_listings = hotel_listings.query.filter_by(id=order.hotel_id).first()

        orderblock = orderblock + """ <tr>
                                         <th scope="row">{}</th>
                                         <td>{}</td>
                                         <td>{}</td>
                                        <td>{}</td>
                                        <td>{}</td>
                                        <td>{}</td>
                                        <td>${}</td>
                                        </tr>""".format(order.id, order.purchase_date, order.username,
                                                        flight.flight_no if flight is not None else '',
                                                        hotel.hname if hotel is not None else '', order.total_persons,
                                                        order.total_price)
    print(orderblock)
    return render_template('pastorders.html', orderblock=Markup(orderblock))

