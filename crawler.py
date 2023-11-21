import requests
from bs4 import BeautifulSoup
import csv

# initilize list or array to store the scraped data
products = []

# a list of discovered urls with the first one to start
urls = ["https://scrapeme.live/shop/"]

