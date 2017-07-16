import re
from datetime import date
from calendar import monthrange

TEENTH_DAYS = list(range(13, 20))

def meetup_day(year, month, dayname, descriptor):
    #day = 0
    if descriptor == 'teenth':
        for candidate in TEENTH_DAYS:
            if date(year, month, candidate).strftime('%A') == dayname:
                #day = candidate
                return date(year, month, candidate)
    if descriptor == 'last':
        days = monthrange(year, month)[1]
        last_days = range(days - 7 + 1, days + 1)
        for candidate in last_days:
            if date(year, month, candidate).strftime('%A') == dayname:
                return date(year, month, candidate)
    if descriptor[-2:] in ['st', 'nd', 'rd', 'th']:
        enumerator = int(re.findall(r'\d+', descriptor)[0])
        count = 0
        candidate = 1
        try:
            while True:
                if date(year, month, candidate).strftime('%A') == dayname:
                    count += 1
                if count == enumerator:
                    #day = candidate
                    return date(year, month, candidate)
                candidate += 1
        except ValueError:
            raise MeetupDayException('Specified day does not exist.')

    #pass
    #raise MeetupDayException('Specified day does not exist.')
    #return date(year, month, day)

class MeetupDayException(Exception):
    pass
