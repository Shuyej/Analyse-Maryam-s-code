import time
import random
import Scrapelinks
from bs4 import BeautifulSoup

# find category

def categoryfunc(tilli):
    #    tag=tilli.find_all(class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    tag = tilli.find_all('a', class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    category = []

    for w in range(0, len(tag)):
        category.append(tag[w].getText())

    return category
