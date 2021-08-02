import requests

from bs4 import BeautifulSoup

import datetime as dt

import platform

import pyautogui as py

import random

import os

import time

from pyvirtualdisplay import Display

from htmldate import find_date

import pandas as pd

from newspaper import Article


def convert(set):
    return [*set, ]


# scrape links

def scrapeBBlinks(x):
    url = x

    response = driver.get(url)

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


# find menu

# =============================================================================

# def menu1(homelink):

#     driver.get(homelink)

#     #time.sleep(random.randint(1,20))

#     #py.scroll(-(random.randint(200,1000)))

#     html=driver.page_source

#     doc=BeautifulSoup(html,'html.parser')

#     tabs=doc.find_all(class_='nw-o-link')

#     tabshref=[]

#     http=[]

#     https=[]

#     dotcom=[]

#     linkx='https://www.bbc.co.uk'

#     for tab in tabs:

#         if ('href' in str(tab))==True:

#             tabhref=(tab['href'])

#             if ('http' in str(tabhref))==True:

#                 http.append(tabhref)

#             elif ('https' in str(tabhref))==True:

#                 https.append(tabhref)

#             elif ('.com' in str(tabhref))==True:

#                 dotcom.append(tabhref)

#             else:

#                 linky=linkx+tabhref

#                 tabshref.append(linky)

#     uniquetabshrefpuff=set(tabshref)

#     uniquetabshrefpuff=list(uniquetabshrefpuff)

#     uniquetabshref=[]

#     for listunique in uniquetabshrefpuff:

#         if ('news' in str(listunique)) ==True:

#             uniquetabshref.append(listunique)

#         else:

#             continue

#     ##################################

#

#     listfinale=uniquetabshref

#     listfinale1=set(listfinale)

#     listfinale1=list(listfinale1)

#

#     return listfinale1

# =============================================================================

# find author

def authorsfunc(tilli):
    #    authors=tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n1')

    authors = tilli.find_all('p', class_='ssrcss-1a9jc18-Contributor e5xb54n2')

    authauth = []

    if len(authors) >= 1:

        for w in range(0, len(authors)):
            authauth.append(authors[w].getText())

    return authauth


# find date

def datefunc(tilli):
    datepuff = tilli.find_all('time')

    if len(datepuff) >= 1:

        datex = tilli.find_all('time')[0]['datetime']

    else:

        datex = None

    return datex


# find title

def titlefunc(tilli):
    Title = tilli.find_all('h1')

    if len(Title) > 0:
        Title = Title[0].getText()

    return Title


# find category

def categoryfunc(tilli):
    #    tag=tilli.find_all(class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    tag = tilli.find_all('a', class_='ssrcss-1yno9a1-StyledLink ed0g1kj0')

    category = []

    for w in range(0, len(tag)):
        category.append(tag[w].getText())

    return category


# scrape every single links and find texts

def scrapeBB(z):
    finaltext = []

    finddate = []

    finddate2 = []

    findauthors = []

    findtitle = []

    findcategory = []

    for i in range(0, len(z)):

        # time.sleep(random.randint(1,20))

        # py.scroll(-(random.randint(200,1000)))

        driver.get(z[i])

        # driver.get('https://www.bbc.co.uk/news/av/science-environment-56690950')

        html = driver.page_source

        doc = BeautifulSoup(html, 'html.parser')

        #####finding paragraphs

        if (doc.find_all("p", class_='ssrcss-1q0x1qg-Paragraph eq5iqo00') == []):

            textarticle = doc.find_all("p", class_='')

        else:

            textarticle = doc.find_all("p", class_='ssrcss-1q0x1qg-Paragraph eq5iqo00')

        text = []

        a = ['.', '?', '!', ':']

        b = ['We use cookies to give you the best online experience',

             'Please let us know if you agree to all of these cookies',

             'The BBC is not responsible', 'Read about our', '©',

             'Let us know you agree to cookies', '2021 BBC',

             'The BBC is not responsible for the content of external sites.',

             'Read about our approach to external linking.']

        for j in range(0, len(textarticle)):

            # adverts

            if (textarticle[j].find_all('i') == []):

                t = textarticle[j].getText()

                if any(x in t for x in a):

                    if all(w not in t for w in b):
                        text.append(t)

                else:

                    continue

            else:

                continue

        ######finding lists

        bulletpoint = doc.find_all(class_="ssrcss-1pzprxn-BulletListContainer e5tfeyi0")

        bulletpoint1 = []

        for j in range(0, len(bulletpoint)):
            bulletpoint1.append(bulletpoint[j].find_all('li', class_=[]))

        textlist = []

        for j in range(0, len(bulletpoint1)):

            for w in range(0, len(bulletpoint1[j])):
                textlist.append(bulletpoint1[j][w].getText() + '.')

        ######text plus paragraph

        text1 = text + textlist

        #######concat text+paragraph

        textfinal = text1[0]

        for w in range(1, len(text1)):
            textfinal = textfinal + ' ' + text1[w]

        authorit = authorsfunc(doc)

        tagit = categoryfunc(doc)

        titleit = titlefunc(doc)

        findauthors.append(authorit)

        findtitle.append(titleit)

        finaltext.append(textfinal)

        findcategory.append(tagit)

        print(i)

        date1 = datefunc(doc)

        finddate.append(date1)

        # finddate1.append(date2)

        finddate2.append(find_date(z[i]))

        # print(finddate,findtitle,findauthors,findcategory,finaltext)

    return finddate, finddate2, findtitle, findauthors, findcategory, finaltext


# scrape all links on the website and find link category

menu = ['https://www.bbc.co.uk/news/technology', 'https://www.bbc.co.uk/news/business',

        'https://www.bbc.co.uk/news/business/your_money', 'https://www.bbc.co.uk/news/business/companies',

        'https://www.bbc.co.uk/news/business/economy', 'https://www.bbc.co.uk/news/business/global_car_industry',

        'https://www.bbc.co.uk/news/business/business_of_sport', 'https://www.bbc.co.uk/news/politics',

        'https://www.bbc.co.uk/news/politics/uk_leaves_the_eu', 'https://www.bbc.co.uk/news/politics/parliaments',

        'https://www.bbc.co.uk/news/coronavirus', 'https://www.bbc.co.uk/news/world', 'https://www.bbc.co.uk/news/uk',

        'https://www.bbc.co.uk/news/world/africa', 'https://www.bbc.co.uk/news/world/asia',
        'https://www.bbc.co.uk/news/world/australia',

        'https://www.bbc.co.uk/news/world/europe', 'https://www.bbc.co.uk/news/world/latin_america',

        'https://www.bbc.co.uk/news/world/middle_east', 'https://www.bbc.co.uk/news/world/us_and_canada',

        'https://www.bbc.co.uk/news/science_and_environment', 'https://www.bbc.co.uk/news/health',

        'https://www.bbc.co.uk/news/education', 'https://www.bbc.co.uk/news/entertainment_and_arts',

        'https://www.bbc.co.uk/news/reality_check', 'https://www.bbc.co.uk/news/the_reporters',

        'https://www.bbc.co.uk/news/newsbeat', 'https://www.bbc.co.uk/news/stories',

        'https://www.bbc.co.uk/news/coronavirus', 'https://www.bbc.co.uk/news/have_your_say',

        'https://www.bbc.co.uk/news/topics/cvenzmgyww4t/space-exploration',

        'https://www.bbc.co.uk/news/topics/c4y3wxdx24nt/our-planet-now',

        ]

linksall = []

for i in range(0, len(menu)):
    linksall.append(scrapeBBlinks(menu[i]))

totallinksall = linksall[0]

for i in range(1, len(linksall)):
    totallinksall = totallinksall + linksall[i]

uniquetotallinks = set(totallinksall)

uniquetotallinks = list(uniquetotallinks)

uniquetotallinks1 = []

a = ['/news/', '/articles/', '/article/']

b = ['send']

for i in range(0, len(uniquetotallinks)):

    if any(x in uniquetotallinks[i] for x in a) and any(x not in uniquetotallinks[i] for x in b):
        uniquetotallinks1.append(uniquetotallinks[i])

# pd.DataFrame(uniquetotallinks).to_csv(r'C:\Users\44798\links.csv')


d, d1, ttl, auth, catg, txt = scrapeBB(uniquetotallinks[:10])

# =============================================================================

#

# ul='https://www.bbc.co.uk/news'

# listlinks=menu1(ul)

#

# nohttps=[]

# https=[]

# for linkala in listlinks:

#     if 'https' not in linkala:

#         nohttps.append(linkala)

#     else:

#         https.append(linkala)

#

# linksall=[]

# for i in range(0,len(https)):

#     linksall.append(scrapeBBlinks(https[i]))

#

# totallinksall=linksall[0]

# for i in range(1,len(linksall)):

#     totallinksall=totallinksall+linksall[i]

#

# uniquetotallinks=set(totallinksall)

# uniquetotallinks=list(uniquetotallinks)

#

# Nofinallinks=[]

# finallinksdone=[]

# for j in range(0,len(uniquetotallinks)):

#     if any(x in uniquetotallinks[j] for x not in https):

#         Nofinallinks.append(uniquetotallinks[j])

#     else:

#         finallinksdone.append(uniquetotallinks[j])

#

# =============================================================================
