
import time
import random
import Scrapelinks
from bs4 import BeautifulSoup
from Webdriver import Webdrivercode

driver = Webdrivercode.driver

# scrape links

def scrapeBBlinks(x):
    url = x
    response = driver.get(url)
    print("New link:" + url)

    # time.sleep(random.randint(10,50))

    # py.scroll(-(random.randint(200,1000)))

    real_soup = BeautifulSoup(driver.page_source, 'html.parser')

    links = real_soup.find_all('a', {'class': 'gs-c-promo-heading'})

    time.sleep(random.randint(1, 10))

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
