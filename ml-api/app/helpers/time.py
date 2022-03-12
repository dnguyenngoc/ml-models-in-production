import datetime
import pytz


def now_utc():
    now = datetime.datetime.utcnow()
    now = now.replace(tzinfo=pytz.utc)
    return now

def str_yyyy_mm_from_int(year, month, space = '-'):
    if month < 10:
        str_month = '0'+ str(month)
    else:
        str_month = str(month)
    return str(year) + space + str_month

def str_yyyy_mm_dd(time: datetime = now_utc(), space = "-"):
    str_year = str(time.year)
    if time.month < 10:
        str_month = '0'+ str(time.month)
    else:
        str_month = str(time.month)
    if time.day < 10:
        str_day = '0'+ str(time.day)
    else:
        str_day = str(time.day)
    return str_year + space + str_month + space + str_day

def str_yyyy_mm(time = now_utc(), space = "-"):
    str_year = str(time.year)
    if time.month < 10:
        str_month = '0'+ str(time.month)
    else:
        str_month = str(time.month)
    return  str_year + space + str_month
