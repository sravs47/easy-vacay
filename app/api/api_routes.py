
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
    """Example endpoint returning a list of Flights
        ---
        tags:
          - restful
        parameters:
          - name: from
            in: query
            type: string
            enum: ['Austin']
            required: true
            description: Source
          - name: to
            in: query
            type: string
            enum: ['Houston']
            required: true
            description: Destination
          - name: starttime
            in: query
            type: string
            enum: ['04/10/2020']
            required: true
            description: Start Date
          - name: count
            in: query
            type: integer
            enum: [1]
            required: true
            description: Count of Passengers
        responses:
          200:
            description: List of flights available for the given date
        """
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
    """Endpoint returning status of the flight for the given flight
            ---
            tags:
              - restful
            parameters:
              - name: flightno
                in: path
                type: string
                enum: ['SW200', 'AA100', 'FR227']
                required: true
                description: Flight Number
              - name: date
                in: query
                type: string
                enum: ['04/10/2020']
                required: true
                description: Departure Date
            responses:
              200:
                description: Gives Flight status
            """
    response = json.dumps(
        [r.as_dict() for r in flight_listings.query.filter(flight_listings.flight_no == flightno,
                                                           flight_listings.starttime == datetime.datetime.strptime(
                                                               request.args['date'], '%m/%d/%Y'))],
        default=utils.datetimeconverter);
    return response


@api_bp.route('/hotels')
def gethotels():
    """Endpoint returning a list of Hotels for the given selection
            ---
            tags:
              - restful
            parameters:
              - name: city
                in: query
                type: string
                enum: ['Dallas']
                required: true
                description: Source
              - name: fromdate
                in: query
                type: string
                enum: ['04/10/2020']
                required: true
                description: Destination
              - name: todate
                in: query
                type: string
                enum: ['04/20/2020']
                required: true
                description: to Date
              - name: count
                in: query
                type: integer
                enum: [1]
                required: true
                description: People count
            responses:
              200:
                description: List of hotels available for the given date & destination
            """
    datas = request.args
    output = json.dumps([r.as_dict() for r in hotel_listings.query.filter(
        hotel_listings.fromdate == datetime.datetime.strptime(datas['fromdate'], '%m/%d/%Y'),
        hotel_listings.rooms >= 1,
        hotel_listings.city == datas['city'])], default=utils.datetimeconverter)
    print(output)
    return output

@api_bp.route('/comments')
def getcomments():
    """Endpoint Gives list of Reviews given by customers
                ---
                tags:
                  - restful
                responses:
                  200:
                    description: Gives comments
                """
    return json.dumps([r.as_dict() for r in testimonals.query.order_by(testimonals.c_date).limit(20)],
                      default=utils.datetimeconverter)

