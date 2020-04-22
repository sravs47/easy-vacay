from flask import Blueprint, request
from app.dbModels.flight_listings import flight_listings
from app.dbModels.hotel_listings import hotel_listings
from app.dbModels.testimonals import testimonals
import datetime
import json
from app.helpers import utils



api_bp = Blueprint('api_bp', __name__, url_prefix='/api')


@api_bp.route('/flights')
def getflights():
    args = request.args
    output = json.dumps([r.as_dict() for r in flight_listings.query.filter(
        flight_listings.starttime == datetime.datetime.strptime(args['starttime'], '%m/%d/%Y'),
        flight_listings.seatcount >= int(args['count']),
        flight_listings.source == args['from'], flight_listings.destination == args['to'])],
                        default=utils.datetimeconverter)
    print(output)
    return output


@api_bp.route('/flightstatus/<flightno>')
def get_flight_status(flightno):
    response = json.dumps(
        [r.as_dict() for r in flight_listings.query.filter(flight_listings.flight_no == flightno,
                                                           flight_listings.starttime == datetime.datetime.strptime(
                                                               request.args['date'], '%m/%d/%Y'))],
        default=utils.datetimeconverter);
    return response


@api_bp.route('/comments')
def getcomments():
    return json.dumps([r.as_dict() for r in testimonals.query.order_by(testimonals.c_date).limit(20)],
                      default=utils.datetimeconverter)