import datetime

def add_gigasecond(indate):
    return indate + datetime.timedelta(seconds=10**9)
