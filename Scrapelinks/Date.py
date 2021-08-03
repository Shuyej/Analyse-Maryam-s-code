
import datetime as dt
from htmldate import find_date

# find date

def datefunc(tilli):
    datepuff = tilli.find_all('time')

    if len(datepuff) >= 1:

        datex = tilli.find_all('time')[0]['datetime']

    else:

        datex = None

    return datex