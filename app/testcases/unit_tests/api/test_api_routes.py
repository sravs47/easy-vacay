
from unittest import TestCase
from unittest.mock import patch, Mock
from app.api import api_routes
import ast

class TestAPI(TestCase):
    @patch('app.api.api_routes.request')
    @patch('app.api.api_routes.flight_listings')
    @patch('app.api.api_routes.datetime')
    def testgetflights(self, mock_requests, mock_flight_listings, mock_datetime):
        mock_requests.args = {'starttime': '04102020', 'count': 20, 'from': 'Austin', 'destination': 'Houston'}
        mock_datetime.datetime.datetime.strptime = mock_requests.args['starttime']
        mock_flight_listings.seatcount = 20
        mock_flight_listing1 = Mock()
        mock_flight_listing1.as_dict.return_value = {'starttime': mock_datetime.datetime.datetime.strptime,
                                                     'seatcount': 20, 'source': mock_requests.args['from'],
                                                     'destination': mock_requests.args['destination']}
        mock_flight_listings.query.filter.return_value = [mock_flight_listing1]

        response = api_routes.getflights()
        res = ast.literal_eval(response)
        res_dict = res.pop()
        assert isinstance(response, str)
        assert isinstance(res, list)
        assert res_dict['seatcount'] == 20
        assert res_dict['starttime'] == '04102020'
        assert res_dict['source'] == 'Austin'
        assert res_dict['destination'] =='Houston'

    @patch('app.api.api_routes.request')
    @patch('app.api.api_routes.hotel_listings')
    @patch('app.api.api_routes.datetime')
    def testgethotels(self, mock_request, mock_hotel_listings, mock_datetime):
        mock_request.args.return_value = {'fromdate':'04102020', 'rooms':2, 'city':'Houston'}
        mock_hotel_listings.rooms = 2
        mock_hotel_listings1 =  Mock()
        mock_hotel_listings1.as_dict.return_value = {'fromdate':'04102020','rooms':2, 'city':'Houston'}
        mock_hotel_listings.query.filter.return_value =[mock_hotel_listings1]
        response = api_routes.gethotels()
        res = ast.literal_eval(response)
        res_dict = res.pop()
        assert isinstance(response,str)
        assert res_dict['fromdate'] == '04102020'
        assert res_dict['rooms'] == 2
        assert res_dict['city'] == 'Houston'


    @patch('app.api.api_routes.testimonals')
    def testgetcomments(self, mock_testimonals):

        mock_testimonals1 = Mock()
        mock_testimonals1.as_dict.return_value = {"id": 9, "username": "sravs47", "comment": "hi", "rating": 4,
                                                  "c_date": "2020-04-03 15:58:17"}
        mock_testimonals.c_date = "2020-04-03 15:58:17"
        mock_testimonals.query.order_by.limit.return_value = [mock_testimonals1]
        response = api_routes.getcomments()
        assert isinstance(response,str)


    @patch('app.api.api_routes.flight_listings')
    @patch('app.api.api_routes.request')
    @patch('app.api.api_routes.datetime')
    def test_get_flight_status(self,flight_listings, mock_requests, mock_datetime):

        mock_requests.args.return_value = {'date':'04102020'}
        flight_listings1 = Mock()
        flight_listings1.as_dict.return_value = {'flight_no':'117','starttime':'04102020'}
        mock_datetime.datetime.datetime.strptime = mock_requests.args['date']
        flight_listings.query.filter.return_value = [flight_listings1]
        response = api_routes.get_flight_status(117)
        assert isinstance(response,str)










