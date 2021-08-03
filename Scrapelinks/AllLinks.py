
import Scrapelinks
from bs4 import BeautifulSoup
import datetime as dt

driver = Scrapelinks.Webdrivercode.driver
authorsfunc = Scrapelinks.FindAuthors.authorsfunc
titlefunc = Scrapelinks.Titlefunc.titlefunc
categoryfunc = Scrapelinks.categoryfunc.categoryfunc
# scrape every single links and find texts
datefunc = Scrapelinks.Date.datefun

def scrapeBB(z):
    finaltext = [] #to store all final text
    finddate = []  #to store all dates
    finddate2 = [] #to store more dates
    findauthors = [] #to add all authors
    findtitle = [] #to add all titles
    findcategory = [] #to add all categories

    for i in range(0, len(z)): #z is the variable passed through the function ScrapeBB
        # time.sleep(random.randint(1,20))
        # py.scroll(-(random.randint(200,1000)))
        driver.get(z[i]) #driver of each url found, of which are in the range of the url passed
        # driver.get('https://www.bbc.co.uk/news/av/science-environment-56690950')
        html = driver.page_source #find page source of web page, which is stored as html
        doc = BeautifulSoup(html, 'html.parser') #convert the page found and add it to html types

        #####finding paragraphs

        if (doc.find_all("p", class_='ssrcss-1q0x1qg-Paragraph eq5iqo00') == []):
            textarticle = doc.find_all("p", class_='')
#for each file within doc, that is within the given class, which has element p of which is an empty list,
#you want to update all elements with finding all the p element, for all classes and store values within textarticle
#As a result you find all paragraphs
        else:
            textarticle = doc.find_all("p", class_='ssrcss-1q0x1qg-Paragraph eq5iqo00')
            #if list is not empty then you add information from the original class. Notice to use a class we use class_ #underscore is essential

        text = [] #create an empty list

        a = ['.', '?', '!', ':'] #creare a list that has all puncutation of relevance
        b = ['We use cookies to give you the best online experience',
             'Please let us know if you agree to all of these cookies',
             'The BBC is not responsible', 'Read about our', '©',
             'Let us know you agree to cookies', '2021 BBC',
             'The BBC is not responsible for the content of external sites.', 'Read about our approach to external linking.']
#b lists all the information to let the user know their data will be used
        for j in range(0, len(textarticle)):  #textarticle is the variable created from the previous lines of codes

            # adverts
            if (textarticle[j].find_all('i') == []): #for each text article within the range of possible text articles
                #if statement creates the following if there is a empty list within text article, i elements
                t = textarticle[j].getText() #find all the text
                if any(x in t for x in a): #x is a variable within the variable that extracts all text #recall a stores all punctuation
                   #so for any x stored inside the variable that stores text, while x also is a puncuation --> Way to read the line
                    if all(w not in t for w in b): #w is a variable within the variable that does not extract all text #recsall b displays information about cookies
                        #so for any w not in the variable that stores text, while  w is also inside the variable that stores information
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
       #

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
