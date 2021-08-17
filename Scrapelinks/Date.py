
import datetime as dt
from htmldate import find_date

# find date
def datefunc(tilli):
    datepuff = tilli.find_all('time')
    #variable datepuff stores values from tilli and its time elements. This varies accordign to the variable passed thriugh the paranthesis (for which is recognised as Tilli)

    if len(datepuff) >= 1: #if the total elements within datepuff, which varies according to the variable tilli passed through date func, is greater than or equal to 1
        datex = tilli.find_all('time')[0]['datetime'] #we store the variable datex which consists of time elements amd date time elements

    else:
        datex = None #return the none type variable which simply states None i.e. integer is a variable type so is None

    return datex #return the variable of interest