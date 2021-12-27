import pandas as pd
from requests_html import HTMLSession

import time

# url = 'https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1'
session = HTMLSession()
drink_list = []

def request(url):
    r = session.get(url)
    # render the page, use sleep param if things aren't working
    r.html.render(sleep=1)
    return r.html.xpath('//*[@id="product-items-container"]', first=True)

def parse(products):
    for item in products.absolute_links:
        r = session.get(item)
        # only render the main page, not each product page
        name = r.html.find('div.product-detail-info-title', first=True).text
        subtext = r.html.find('div.product-subtext', first=True).text
        price = r.html.find('span.price', first=True).text
        
        try:
            rating = r.html.find('span.label-stars', first=True).text
        except:
            rating = 'none'

        if r.html.find('div.add-to-cart-container'):
            stock = 'in stock'
        else:
            stock = 'out of stock'
        
        drink = {
            'name': name,
            'subtext': subtext,
            'price': price,
            'rating': rating,
            'stock': stock,
        }
        drink_list.append(drink)

def output():
    df = pd.DataFrame(drink_list)
    df.to_csv('drinks.csv', index=False)
    print('Saved to CSV file')



x = 1
while True:
    try:
        products = request(f'https://www.beerwulf.com/en-gb/c/all-beers?segment=Beers&catalogCode=Beer_1&routeQuery=all-beers&page={x}')
        print(f'Getting items from page {x}')
        parse(products)
        print('Total items: ', len(drink_list))
        x += 1
        time.sleep(2)
    except:
        print('no more items')
        break
output()