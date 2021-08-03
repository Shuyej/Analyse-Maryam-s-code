
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from fake_useragent import UserAgent

# set up drive
options = webdriver.ChromeOptions() #access option feature and store its values in the variable options

unpacked_extension_path = r'D:\repo\github.com\NLP\bypass-paywalls-chrome-master' #link to extension  file created on Github

options.add_argument(f'--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '

                     f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 '

                     f'Edge/12.10166"') #Add command line window when starting Chrome

options.add_argument(f'user-agent={UserAgent}') ##Add fake user option to Chrome so company, BBC, will not know you accessed their file

options.add_argument("start-maximized") #Open chrome on a maximised window

options.add_argument('--load-extension={}'.format(unpacked_extension_path)) #Add extension to Chrome

options.add_experimental_option("excludeSwitches", ["enable-automation"]) #Allows chrome to be controlled by a automated test software

options.add_experimental_option('useAutomationExtension', False) #do not use automated extension, which is different to automated test software

# driver=webdriver.Chrome(chrome_path,chrome_options=options)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
#Sop open Google Chrome driver, install it, with additional options. These options have been specified as seen in the line of codes above

