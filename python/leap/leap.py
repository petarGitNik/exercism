def is_leap_year(year):
    """
    Find if a year is a leap year.
    """
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        else:
            # If a year is divisible by 100, but ...
            if year % 400 != 0:
                return False
            else:
                return True
        if year % 400 == 0:
            return True
        return True
    # If a year is not divisible by 4, the it is not a candidate to
    # be a leap year
    return False
