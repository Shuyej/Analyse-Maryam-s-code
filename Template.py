import time
import random
import Scrapelinks
from bs4 import BeautifulSoup
from Scrapelinks.BBClinks import *
from Scrapelinks.AllLinks import *

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
        'https://www.bbc.co.uk/news/topics/c4y3wxdx24nt/our-planet-now'] #list of all URLs of interest

linksall = [] #create a empty list to store all data

for i in range(0, len(menu)): #create the sequence for which the BBlinks will be appended based of each element from menu
        #length of array is based off menu
    linksall.append(scrapeBBlinks(menu[i]))

totallinksall = linksall[0] #Store first elements of the array linksall inside totallinksall

for i in range(1, len(linksall)): #The sequence is based of the length from 1 to linksall whrre links all has elements stored from the functions scrapeBBlinks
    totallinksall = totallinksall + linksall[i]  #total linksall ammended from the initial value of linksall[0] adding further elements i.e. from 1 to len(linksall)

uniquetotallinks = set(totallinksall) #convert the variable totallinksall with iteretable elements to distinct elements
# An iteration is when is a repetition of a process, since totallinksall has elements added it is a iterated process
uniquetotallinks = list(uniquetotallinks)
#list takes a iteratble object which is uniquetotallinks and adds its element to a newly created list
uniquetotallinks1 = [] #create an empty list

a = ['/news/', '/articles/', '/article/']
b = ['send']

for i in range(0, len(uniquetotallinks)):
    if any(x in uniquetotallinks[i] for x in a) and any(x not in uniquetotallinks[i] for x in b):
        uniquetotallinks1.append(uniquetotallinks[i])

# pd.DataFrame(uniquetotallinks).to_csv(r'C:\Users\44798\links.csv')
d, d1, ttl, auth, catg, txt = scrapeBBlinks(uniquetotallinks[:10])

scrapeBB(menu)