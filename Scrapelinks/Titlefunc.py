import time
import random
import Scrapelinks
from bs4 import BeautifulSoup


# find title
def titlefunc(tilli):
    Title = tilli.find_all('h1')

    if len(Title) > 0:
        Title = Title[0].getText()

    return Title

