import time
import random
import Scrapelinks
from bs4 import BeautifulSoup

# find title
def titlefunc(tilli):
    Title = tilli.find_all('h1')
#variable Title stores all h1 elements of the variable tilli passing through the paranthesis

    if len(Title) > 0: #if the total no. of elements within TItle, which varies according to the variable paassed through the paranthesis, is greater than 0 then
        Title = Title[0].getText() #for the first element of Title we recieve the text element

    return Title #We return the variable Title

