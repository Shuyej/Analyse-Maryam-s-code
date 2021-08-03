
from bs4 import BeautifulSoup

#find authors
def authorsfunc(tilli):
    #    authors=tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n1')

    authors = tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n2')

    authauth = []

    if len(authors) >= 1:

        for w in range(0, len(authors)):
            authauth.append(authors[w].getText())

    return authauth