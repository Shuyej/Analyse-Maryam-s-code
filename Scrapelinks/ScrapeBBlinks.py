from Scrapelinks.BBClinks import * #utilise all functions from file BBClinks



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

a = ['/news/', '/articles/', '/article/'] #create a list with strings
b = ['send'] #create a list with a string

for i in range(0, len(uniquetotallinks)):
    if any(x in uniquetotallinks[i] for x in a) and any(x not in uniquetotallinks[i] for x in b):
    #Any means an or statement in boolean terms
    #So for x in a means, that x is the variable that passes through each element in a
    #Therefore, while this is going on, and we have a element x that passes through each element of uniquetotallinks
    #Then, from that nested for loop, if we also have in the for loop where the variable x reads through elements of the list b
    #We need for each element accessed through the variable x, not in uniquetotallinks, to be the same
    #While elements for both nested for loops are the same then uniquetotallinks1 will be appended using uniquetotallinks
        uniquetotallinks1.append(uniquetotallinks[i])

# pd.DataFrame(uniquetotallinks).to_csv(r'C:\Users\44798\links.csv')
d, d1, ttl, auth, catg, txt = scrapeBBlinks(uniquetotallinks[:10])
#each of the elements of unique totallinks up to the sequence 10, go through the function scrapeBBlinks

def convert(set): #function converts multiple items into a single variable
    return [*set, ] #set stores multiple items into a single variable of which is *set

