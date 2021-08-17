import time #package provides many ways of representing time in code, such as objects, numbers, and strings
import random #generates random numbers
import Scrapelinks #import the package that was created
from bs4 import BeautifulSoup
from Webdriver import Webdrivercode #File webdrivercode will be used which has function webdrivercode, of the package Webdriver

driver = Webdrivercode.driver
# scrape links

def scrapeBBlinks(x):
    url = x #variable passed through the paranthesis is stored in the variable url
    response = driver.get(url) #use webdriver to get the URL and store it inside variable response

    # time.sleep(random.randint(10,50))
    # py.scroll(-(random.randint(200,1000)))
    real_soup = BeautifulSoup(driver.page_source, 'html.parser') #extract html elements
    links = real_soup.find_all('a', {'class': 'gs-c-promo-heading'}) #find all a tag for the class gs-c...
    time.sleep(random.randint(1, 10)) #stops the current thread for a number of seconds
    #randint returns a random number between the ranges 1 to 10
    #in other words execution stopped between 1 to 10 seconds, but this is done at random

    UL = 'https://www.bbc.co.uk'
    linktext = []
    linkaddress = []
    linkaddresshttp = []

    linkh = []

    for link in links:
        if "Live" in link.text:
            continue
        else:
            linktext.append(link.text)
        linkhref = link['href']
        linkh.append(linkhref)
        if "live" in linkhref:
            continue
        elif "https" and "http" in linkhref:
            linkaddresshttp.append(linkhref)
        else:
            address = UL + linkhref
            linkaddress.append(address)

    linktextset = set(linktext)
    linktextexredundancy = list(linktextset)
    linkaddressset = set(linkaddress)
    linkaddressexredundancy = list(linkaddressset)
    linkaddresshttpset = set(linkaddresshttp)
    linkaddresshttpexredundancy = list(linkaddresshttpset)
    linkaddresstotal = linkaddresshttpexredundancy + linkaddressexredundancy

    return linkaddresstotal
