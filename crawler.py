import requests
from bs4 import BeautifulSoup
import queue
import re
import csv

# initilize list or array to store the scraped data
products = []

# create queue
urls = queue.PriorityQueue()
urls.put((0.5, "https://scrapeme.live/shop/"))

visited_urls = []

# continue until all urls have been visited
while not urls.empty() and len(visited_urls) < 50:
    #ignore the priority value
    _, current_url = urls.get()
    
    response = requests.get(current_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # add current url to visited
    visited_urls.append(current_url)
    
    link_elements = soup.select("a[href]")
    
    for element in link_elements:
        url = element["href"]
        if "https://scrapeme.live/shop" in url:
            if url not in visited_urls and url not in [item[1] for item in urls.queue]:
                #default score
                priority_score = 1
                #if it is a pagination page
                if re.match(r"^https://scrapeme\.live/shop//\d+/?$", url):
                    priority_score = 0.5
                urls.put((priority_score, url))
            
    # if the current url is a product page
    product = {}
    product["url"] = current_url
    product["image"] = soup.select_one(".wp-post-image")["src"]
    product["name"] = soup.select_one(".product_title")
    product["price"] = soup.select_one(".price")
    
    products.append(product)
    
# initialize the CSV
with open('products.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    
    # to populate the csv
    for product in products:
        writer.writerow(product.values())