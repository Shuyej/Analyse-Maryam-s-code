import time
import random
import Scrapelinks
from bs4 import BeautifulSoup
from Scrapelinks.BBClinks import *
from Scrapelinks.AllLinks import *
from Scrapelinks.ScrapeBBlinks import *

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

scrapeBB(menu)