import datetime

def datetimeconverter(o):
    if isinstance(o, datetime.date):
        return o.__str__()
