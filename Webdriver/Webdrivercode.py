
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from fake_useragent import UserAgent

# set up drive
options = webdriver.ChromeOptions() #access option feature and store its values in the variable options

unpacked_extension_path = r'D:\repo\github.com\NLP\bypass-paywalls-chrome-master'

options.add_argument(f'--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) '

                     f'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 '

                     f'Edge/12.10166"')

# options.add_argument(f'user-agent={userAgent}')

options.add_argument("start-maximized")

options.add_argument('--load-extension={}'.format(unpacked_extension_path))

options.add_experimental_option("excludeSwitches", ["enable-automation"])

options.add_experimental_option('useAutomationExtension', False)

# driver=webdriver.Chrome(chrome_path,chrome_options=options)

driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)

