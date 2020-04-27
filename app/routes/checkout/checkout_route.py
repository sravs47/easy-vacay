
from flask import Blueprint, render_template, request, session
from app.dbModels.flight_listings import flight_listings
from app.dbModels.order_history import order_history
from app.dbModels.hotel_listings import hotel_listings
from app.helpers.loginHelper import is_logged_in
from app import db
from app.helpers.checkoutHelper import hotel_li_block, flight_li_block
from jinja2 import Markup

checkout_bp = Blueprint('checkout_bp', __name__, template_folder='app/templates')



@checkout_bp.route('/checkout', methods=["POST", "GET"])
@is_logged_in
def checkout():
    args = request.args
    hotelselection = args.get("hotelselection", None)
    flightselection = args.get("flightselection", None)
    totalcount = args.get("ppl", 0)
    flightdata = None
    hoteldata = None
    if request.method == "POST":
        orders = order_history(username=session['username'],
                               flight_id=flightselection, hotel_id=hotelselection,
                               order_status='incomplete', total_persons=totalcount)
        db.session.add(orders)
        db.session.commit()

    orderblock = ''
    order: order_history = order_history.query.filter_by(username=session['username'],
                                                         order_status='incomplete').order_by(
        order_history.id.desc()).first()
    flight_ids = []
    hotel_ids = []
    amount = 0
    if order is not None and order.flight_id is not None:
        flight_ids.append(order.flight_id)
    if order is not None and order.hotel_id is not None:
        hotel_ids.append(order.hotel_id)

    for flight_id in flight_ids:  # write for loop for orders. get flight listings and hotel listings in a list
        flightlisting: flight_listings = flight_listings.query.filter_by(id=flight_id).first()
        print((flightlisting.starttime).strftime('%m/%d/%Y'))
        print(str(flightlisting.amount))
        orderblock = orderblock + flight_li_block.format(flightlisting.airlines,
                                                         flightlisting.flight_no, flightlisting.source,
                                                         flightlisting.destination, flightlisting.begins,
                                                         flightlisting.ends,
                                                         (flightlisting.starttime).strftime('%m/%d/%Y'),
                                                         str(flightlisting.amount))

        amount = amount + flightlisting.amount * order.total_persons

    for hotel_id in hotel_ids:
        hotellisting: hotel_listings = hotel_listings.query.filter_by(id=hotel_id).first()

        orderblock = orderblock + hotel_li_block.format(hotellisting.hname, hotellisting.city, hotellisting.fromdate,
                                                        hotellisting.todate, hotellisting.hprice)

        amount = amount + hotellisting.hprice * order.total_persons
    orderblock = orderblock + """<li class="list-group-item d-flex justify-content-between lh-condensed">
                        <div>
                            <h6 class="my-0"> Summary:  </h6>
                            <small class="text-muted">Total Persons: {}</small>
                        </div>
                        <span class="text-muted">Total Amount: ${}</span>
                    </li>""".format(order.total_persons if order is not None else 0, amount)

    return render_template('checkout.html', orderblock=Markup(orderblock),
                           amount=round(float(amount) * float(0.8)) if len(flight_ids) > 0 and len(
                               hotel_ids) > 0 else amount)
