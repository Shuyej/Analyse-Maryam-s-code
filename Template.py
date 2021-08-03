import time
import random
import Scrapelinks
from bs4 import BeautifulSoup
from Scrapelinks.BBClinks import *
#Example:

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

#     return listfinale1

# =============================================================================

# find author
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
        'https://www.bbc.co.uk/news/topics/c4y3wxdx24nt/our-planet-now']

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

d, d1, ttl, auth, catg, txt = scrapeBBlinks(uniquetotallinks[:10])