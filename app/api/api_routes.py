from flask import Blueprint, render_template, request
from app import app
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


