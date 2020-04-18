from unittest.mock import patch,Mock
from app.routes.login.login_route import login
from unittest import TestCase


class test_login_route(TestCase):

    @patch('app.routes.login.login_route.request')
    @patch('app.routes.login.login_route.render_template', return_value = 'register.html')
    @patch('app.routes.login.login_route.users')
    @patch('app.routes.login.login_route.session')
    @patch('app.routes.login.login_route.flash')
    @patch('app.routes.login.login_route.url_for')
    @patch('app.routes.login.login_route.redirect',return_value = 'index')
    def test_login_positive(self,mock_redirect,mock_url_for,mock_flash,mock_session,mock_users,mock_render_template,mock_request ):
        mock_users1 = Mock()
        mock_users1.miles = 1213
        mock_request.method = "POST"
        mock_request.form = {'username':'sravani','password':'sravani'}
        mock_session.return_value = {'logged_in':True, 'username':'sravani','miles':1212}
        mock_users.query.filter_by.return_value = mock_users1
        response = login()
        assert response == 'index'

    @patch('app.routes.login.login_route.request')
    @patch('app.routes.login.login_route.render_template')
    @patch('app.routes.login.login_route.users')
    @patch('app.routes.login.login_route.session')
    def test_login_negative1(self, mock_session, mock_users, mock_render_template,
                   mock_request):
        mock_users1 = Mock()
        mock_users1.miles = 1213
        mock_request.method = "POST"
        mock_request.form = {'username': 'sravani', 'password': 'sravani'}
        mock_session.return_value = {'logged_in': True, 'username': 'sravani', 'miles': 1212}
        mock_render_template.return_value = 'register.html'
        mock_users.query.filter_by.return_value = None
        response = login()
        assert response == 'register.html'

    @patch('app.routes.login.login_route.request')
    @patch('app.routes.login.login_route.render_template',return_value = 'register.html')
    def test_login_negative2(self,mock_render_template,mock_request):
        mock_users1 = Mock()
        mock_users1.miles = 1213
        mock_request.method = "GET"
        response = login()
        assert response == 'register.html'

