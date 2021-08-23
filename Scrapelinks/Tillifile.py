
import datetime as dt
from htmldate import find_date
import time
import random
import Scrapelinks
from bs4 import BeautifulSoup

class Tilli(): #set class to use date, category, title and authors functions
#find date

def datefunc(tilli): #function returns the time element of the object tilli or None
    datepuff = tilli.find_all('time')
    #variable datepuff stores values from tilli and its time elements. This varies accordign to the variable passed thriugh the paranthesis (for which is recognised as Tilli)

    if len(datepuff) >= 1: #if the total elements within datepuff, which varies according to the variable tilli passed through date func, is greater than or equal to 1
        datex = tilli.find_all('time')[0]['datetime'] #we store the variable datex which consists of time elements amd date time elements

    else:
        datex = None #return the none type variable which simply states None i.e. integer is a variable type so is None

    return datex #return the variable of interest

# find category

def categoryfunc(tilli): #function returns a variable category consisting of a tag and its respective text
    #tag=tilli.find_all(class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    tag = tilli.find_all('a', class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')
    #so the variable passed through the function categoryfunc is tilli
    #we want the variable tilli and all its elements within the class  ssrcss-1yno9a1-StyledLink ed0g1kj0

    category = [] #create an empty list called category

    for w in range(0, len(tag)): #W is a element for the sequernce of numbers from 0 to len(tag)
        category.append(tag[w].getText())
        #for each element of the variable tag, we get the text.

    return category #return the variable of interest which is the list of elements within the list category

# find title
def titlefunc(tilli): #function returns the text of the h1 tag of the variable passed through the paranthesis.
    Title = tilli.find_all('h1')
#variable Title stores all h1 elements of the variable tilli passing through the paranthesis

    if len(Title) > 0: #if the total no. of elements within TItle, which varies according to the variable paassed through the paranthesis, is greater than 0 then
        Title = Title[0].getText() #for the first element of Title we recieve the text element

    return Title #We return the variable Title


from bs4 import BeautifulSoup

#find authors
def authorsfunc(tilli): #Function returns the list authauth which is based of p tag of the class ssrcss and its text
    #authors=tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n1')

    authors = tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n2')
#for each element passed through and recognised as tilli, we find the p tag but of the class ssrcsss...
    authauth = [] #create an empty list

    if len(authors) >= 1: #for the total number of elements within tilli.find_all("..") being atleast 1

        for w in range(0, len(authors)): #then for the sequence of numbers from 0 to the length of authors, range accessed through the variable w
            authauth.append(authors[w].getText()) #We append the elements within authauth with text

    return authauth #variable of interest returned
