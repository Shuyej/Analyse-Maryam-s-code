
from bs4 import BeautifulSoup

#find authors
def authorsfunc(tilli):
    #authors=tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n1')

    authors = tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n2')
#for each element passed through and recognised as tilli, we find the p tag but of the class ssrcsss...
    authauth = [] #create an empty list

    if len(authors) >= 1: #for the total number of elements within tilli.find_all("..") being atleast 1

        for w in range(0, len(authors)): #then for the sequence of numbers from 0 to the length of authors, range accessed through the variable w
            authauth.append(authors[w].getText()) #We append the elements within authauth with text

    return authauth #variable of interest returned