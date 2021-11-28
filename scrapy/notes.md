scrapy startproject <projectname>
cd into the project and write scrapy shell
next, fetch(<url>) // as string

everything is saved in the response variable, which we can access by typing response

response.css(<tag>.<class>)
e.g. response.css('div.product-item-info') or response.css('article.card')

get first item with response.css(<tag>.<class>).get()

save as variable, products = response.css('article.card')

go deeper:
products.css('p.card-text--brand).get()

get text:
products.css('p.card-text--brand::text').get()

get names from all products
products.css('p.card-text--brand::text).getall()

can use xpath if can't find a class:
products.xpath('//*[@id="product-listing-container"]/form/ul/li[8]/article/figure/a').attrib['href']

make a spider and then use: scrapy crawl <spidername>

output to json with
scrapy crawl <spidername> -O <filename>.json
// big O overwrites any previous file w same name, while little o will append

if you have something like response.css('a.action next') and it doesn't work, try response.css('a.action.next')

with xpath and ItemLoaders, use following format:
l.add_xpath('link', '//*[@id="product-listing-container"]/form/ul/li[8]/article/figure/a/@href')

vs l.add_css('link', 'a.product-item-link::attr(href)')