import requests
from bs4 import BeautifulSoup
import csv

# initilize list or array to store the scraped data
products = []

# a list of discovered urls with the first one to start
urls = ["https://scrapeme.live/shop/"]

# continue until all urls have been visited
while len(urls) != 0:
    # get the page to visit from the list
    current_url = urls.pop()
    
    responce = requests.get(current_url)
    soup = BeautifulSoup(responce.content, 'html.parser')
    
    link_elements = soup.select("a[href]")
    
    for element in link_elements:
        url = element["href"]
        if "https://scrapeme.live/shop" in url:
            urls.append(url)