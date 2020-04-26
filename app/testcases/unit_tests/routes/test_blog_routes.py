from unittest.mock import patch, Mock
from unittest import TestCase
patch('app.helpers.loginHelper.is_logged_in',lambda x:x).start()
from app.routes.blog.blog_routes import blog
from app.routes.blog import blog_routes


class testBlogRoutes(TestCase):

    @patch('app.routes.blog.blog_routes.request')
    @patch('app.routes.blog.blog_routes.testimonals')
    @patch('app.routes.blog.blog_routes.is_logged_in')
    def test_blog(self,mock_request,mock_testimonals,mock_patch):
        blog_routes.is_logged_in = mock_patch
        mock_request.method = 'POST'
        mock_request.form.return_value = {'comment':'some comment', 'rate':'2'}
        response =blog()




