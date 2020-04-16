from app.helpers import utils
from unittest import TestCase
import  datetime

class TestUtils(TestCase):

    def testDateTimeConvert1(self):
        current_time =datetime.date.today()
        print(utils.datetimeconverter(current_time))
        self.assertTrue(isinstance(utils.datetimeconverter(current_time),str))

    def testDateTimeConvert2(self):
        date = datetime.date(2019,4,3)
        print(utils.datetimeconverter(date))

    def testDateTimeConvertNegative1(self):
        current_time ='1/2/2020'
        self.assertFalse(isinstance(utils.datetimeconverter(current_time), str))

    def testDateTimeConvertNegative2(self):
        current_time =datetime.date.today()
        print(utils.datetimeconverter(current_time))


