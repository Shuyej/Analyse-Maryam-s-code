
from Scrapelinks import FindAuthors, Titlefunc, Categoryfunc, Date
import Webdriver
from bs4 import BeautifulSoup
from htmldate import find_date

driver = Webdriver.Webdrivercode.driver
authorsfunc = FindAuthors.authorsfunc
titlefunc = Titlefunc.titlefunc
categoryfunc = Categoryfunc.categoryfunc
# scrape every single links and find texts
datefunc = Date.datefunc

def scrapeBB(z):
    finaltext = [] #to store all final text
    finddate = []  #to store all dates
    finddate2 = [] #to store more dates
    findauthors = [] #to add all authors
    findtitle = [] #to add all titles
    findcategory = [] #to add all categories

    for i in range(0, len(z)): #z is the variable passed through the function ScrapeBB
        #range generates a sequence of numbers
        # time.sleep(random.randint(1,20))
        # py.scroll(-(random.randint(200,1000)))
        driver.get(z[i]) #driver of each url found, of which are in the range of the url passed
        # driver.get('https://www.bbc.co.uk/news/av/science-environment-56690950')
        html = driver.page_source #find page source of web page, which is stored as html
        doc = BeautifulSoup(html, 'html.parser') #convert the page found and add it to html types #bs variable

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
            # adverts #i tag is italic
            if (textarticle[j].find_all('i') == []):  # for each text article within the range of possible text articles
                print(textarticle[j]);
                print("Hello")
                exit()  # print
                # if statement creates the following if there is a empty list within text article, i elements
                t = textarticle[j].getText()  # find all the text
                if (any(x in t for x in a) and all(w not in t for w in b)): #true or false #all needs all to be true #any is one true
                    text.append(t)

                # x is a variable within the variable that extracts all text #recall a stores all punctuation
                # so for any x stored inside the variable that stores text, while x also is a puncuation --> Way to read the line
                # w is a variable within the variable that does not extract all text #recsall b displays information about cookies
                # so for any w not in the variable that stores text, while  w is also inside the variable that stores information
                # append text based on the if statements produced
                # It is alright to have an if within a if but best not to use. Therefore use Boolean Logic
                else:
                    continue #next iteration operated

            else:
                continue #next iteration operated

        ######finding lists

        bulletpoint = doc.find_all(class_="ssrcss-1pzprxn-BulletListContainer e5tfeyi0") #specify class of interest
        bulletpoint1 = [] #create an empty list

        for j in range(0, len(bulletpoint)): #bulletpoint is a variable storing all elements of class
            bulletpoint1.append(bulletpoint[j].find_all('li', class_=[])) #add elements the length of bullet point
        #add elements within the empty pist for all classes which have element list

        textlist = [] #create an empty list

        for j in range(0, len(bulletpoint1)):  #bullet point1 is a list, so you find for within 0 to the length of the list, there is a variable j
            for w in range(0, len(bulletpoint1[j])): #so for the range of values from line 81, you want to access each value through the variable w
                textlist.append(bulletpoint1[j][w].getText() + '.') #then you want to add each element to the list text element
                #as you are working with each individual list, you use append
                #we always use append, not append

        ######text plus paragraph
        text1 = text + textlist #text stores all the elements added from text and text list
        #######concat text+paragraph
        textfinal = text1[0] #store the value of the first element of text1 inside the variable textfinal

        for w in range(1, len(text1)): #text 1 is a list, so you generate a sequence of number of length from 0 to size of text1
            textfinal = textfinal + ' ' + text1[w] #final text is the first element of text 1 to each element within length of text1

        authorit = authorsfunc(doc) #document passes through function
        tagit = categoryfunc(doc) #document passes through function
        titleit = titlefunc(doc) #document passes through function
        findauthors.append(authorit) #findauthors is a function
        findtitle.append(titleit) #findtitle is a function
        finaltext.append(textfinal) #finaltext is a function
        findcategory.append(tagit) #find category is a function

       # print(i)

        date1 = datefunc(doc) #date 1 stores the values generated by function datefunc
        finddate.append(date1) #finddate is a built in function and you want to add dates based on what is passed through date 1
        # finddate1.append(date2)
        finddate2.append(find_date(z[i])) #append based on find_date
        # print(finddate,findtitle,findauthors,findcategory,finaltext)
    return finddate, finddate2, findtitle, findauthors, findcategory, finaltext
