#import requests
#import platform
#import pyautogui as py
#import os
#from pyvirtualdisplay import Display
#import pandas as pd

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