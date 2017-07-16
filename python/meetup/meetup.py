import re
from datetime import date
from calendar import monthrange

TEENTH_DAYS = list(range(13, 20))

def meetup_day(year, month, dayname, descriptor):
    if descriptor == 'teenth':
        return search_seven_days_period(year, month, dayname, descriptor, TEENTH_DAYS)

    if descriptor == 'last':
        days = monthrange(year, month)[1]
        last_days = range(days - 7 + 1, days + 1)
        return search_seven_days_period(year, month, dayname, descriptor, last_days)

    if descriptor[-2:] in ['st', 'nd', 'rd', 'th']:
        enumerator = int(re.findall(r'\d+', descriptor)[0])
        count = 0
        candidate = 1
        try:
            while True:
                if date(year, month, candidate).strftime('%A') == dayname:
                    count += 1
                if count == enumerator:
                    return date(year, month, candidate)
                candidate += 1
        except ValueError:
            raise MeetupDayException('Specified day does not exist.')

def search_seven_days_period(year, month, dayname, descriptor, period):
    for candidate in period:
        if date(year, month, candidate).strftime('%A') == dayname:
            return date(year, month, candidate)

class MeetupDayException(Exception):
    pass
