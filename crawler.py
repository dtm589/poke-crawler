import requests
from bs4 import BeautifulSoup
import csv

# initilize list or array to store the scraped data
products = []

# a list of discovered urls with the first one to start
urls = ["https://scrapeme.live/shop/"]
visited_urls = []

# continue until all urls have been visited
while len(urls) != 0:
    # get the page to visit from the list
    current_url = urls.pop()
    
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # add current url to visited
    visited_urls.append(current_url)
    
    link_elements = soup.select("a[href]")
    
    for element in link_elements:
        url = element["href"]
        if "https://scrapeme.live/shop" in url:
            if url not in visited_urls and url not in urls:
                urls.append(url)
            
    # if the current url is a product page
    product = {}
    product["url"] = current_url
    product["image"] = soup.select_one(".wp-post-image")["src"]
    product["name"] = soup.select_one(".product_title")
    product["price"] = soup.select_one(".amount")
    
    products.append(product)
    
# initialize the CSV
with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    
    # to populate the csv
    for product in products:
        writer.writerow(product.values())