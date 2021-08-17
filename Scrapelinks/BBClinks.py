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

    UL = 'https://www.bbc.co.uk' #URL of Interest
    linktext = [] #Create an empty list
    linkaddress = [] #Create an empty list
    linkaddresshttp = [] #Create an empty list

    linkh = [] #Create an empty list

    for link in links: #link is a variable to access the elements within the list links
        #recall links is in line 17 which is defined as consisting of the a tag within the class gs-c-promo-heading
        if "Live" in link.text: #access the text within the elements of links and find the live element. If this is true then we continue
            continue
        else:
            linktext.append(link.text) #for the elements withink linkstext, append these based on the text from the elements link of the variable links
        linkhref = link['href'] #access href tag of the variable link
        linkh.append(linkhref) #append linkh based on the href tag of the variable link
        if "live" in linkhref: #access the href tag within the variable link and find the live element.
            continue #continue to the next part of he code
        elif "https" and "http" in linkhref: #if http elements of links, stored in linkhref have https and http then line 40 executed
            linkaddresshttp.append(linkhref) #append elements of linkaddresshttp with the values within the variable linkhref
        else:
            address = UL + linkhref #update url address based on the link UL and linkshref variable
            linkaddress.append(address) #append elements within linkaddress with address
    # set converts iretable elements i.e. variables that have elements added based on iteration, with distinct elements

    linktextset = set(linktext) #variable linktext is a list
    linktextexredundancy = list(linktextset) #variable linktextset is a list
    linkaddressset = set(linkaddress) #variable linkaddress is a list
    linkaddressexredundancy = list(linkaddressset) #variable linkaddressset is a list
    linkaddresshttpset = set(linkaddresshttp) #variable linkaddresshttp is a list
    linkaddresshttpexredundancy = list(linkaddresshttpset) #variable linkaddresshttpset is a list
    linkaddresstotal = linkaddresshttpexredundancy + linkaddressexredundancy #create a new variable linkaddresstotal which has all elements created with distinct elements as created by the function list

    return linkaddresstotal #variable returned by the function Scrape BBlinks
