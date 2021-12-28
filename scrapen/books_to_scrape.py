from bs4 import BeautifulSoup
import requests


import logging
from urllib.parse import urljoin


logging.basicConfig(filename='book.log', level=logging.DEBUG,
                    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


url = 'https://books.toscrape.com/catalogue/page-1.html'
base_url = 'https://books.toscrape.com/catalogue/'

try:
    r = requests.get(url)
    r.raise_for_status()
except requests.exceptions.RequestException as err:
    print('Exception found')
    logging.warning(err)

soup = BeautifulSoup(r.text, 'lxml')

articles = soup.find_all('article', class_ = 'product_pod')

for article in articles:
    title = article.h3.text
    price = article.find('p', class_ = 'price_color').text
    availability = article.find('p', class_ = 'instock').text.strip()
    link = urljoin(base_url, article.h3.a['href'])
    book = {
        'title': title,
        'price': price,
        'availability': availability,
        'link': link,
    }
    logging.info(book)