from requests_html import HTMLSession
import time

urls = []
for x in range(1, 51):
    urls.append(f'http://books.toscrape.com/catalogue/page-{x}.html')

# print(len(urls))

def work(url):
    r = s.get(url)
    products = []
    desc = r.html.find('article.product_pod')
    for item in desc:
        product = {
            'title': item.find('h3 a[title]', first=True).text,
            'price': item.find('p.price_color', first=True).text
        }
        products.append(product)
    return products

def main(urls):
    for url in urls:  
        print(work(url))
    return

s = HTMLSession()
start = time.perf_counter()
main(urls)
end = time.perf_counter() - start
print(end) # 6.0757828709999995