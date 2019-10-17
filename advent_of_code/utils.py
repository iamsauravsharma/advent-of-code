import datetime

from dateutil.tz import gettz

EASTERN = gettz("America/New_York")


def get_current_year():
    """
    Get latest year of advent of code return old year if month is not December
    otherwise return current year
    """
    date_time = datetime.datetime.now(tz=EASTERN)
    if date_time.month < 12:
        return date_time.year - 1
    else:
        return date_time


def get_day():
    """
    Get latest day or set a latest day as 1 if this is not month of December
    """
    date_time = datetime.datetime.now(tz=EASTERN)
    if date_time.month == 12:
        return min(date_time.day, 25)
    else:
        return 1
