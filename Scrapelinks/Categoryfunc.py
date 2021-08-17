import time
import random
import Scrapelinks
from bs4 import BeautifulSoup

# find category

def categoryfunc(tilli):
    #tag=tilli.find_all(class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    tag = tilli.find_all('a', class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')
    #so the variable passed through the function categoryfunc is tilli
    #we want the variable tilli and all its elements within the class  ssrcss-1yno9a1-StyledLink ed0g1kj0

    category = [] #create an empty list called category

    for w in range(0, len(tag)): #W is a element for the sequernce of numbers from 0 to len(tag)
        category.append(tag[w].getText())
        #for each element of the variable tag, we get the text.

    return category #return the variable of interest which is the list of elements within the list category
