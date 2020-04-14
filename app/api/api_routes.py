from flask import Blueprint, request
from app.dbModels.flight_listings import flight_listings

import datetime
import json



api_bp = Blueprint('api_bp', __name__, url_prefix='/api')

def datetimeconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()

@api_bp.route('/flightstatus/<flightno>')
def get_flight_status(flightno):
    response = json.dumps(
        [r.as_dict() for r in flight_listings.query.filter(flight_listings.flight_no == flightno,
                                                           flight_listings.starttime == datetime.datetime.strptime(
                                                               request.args['date'], '%m/%d/%Y'))],
        default=utils.datetimeconverter);
    return response

