from unittest import TestCase
from unittest.mock import Mock
from app.helpers.registerHelper import RegisterForm
from wtforms import StringField

Form = Mock()

class TestRegisterHelper(TestCase):

    def TestRegisterForm(self):
         s = RegisterForm(Form)
         print(s)
         self.assertFalse( isinstance(s.firstname,StringField))




