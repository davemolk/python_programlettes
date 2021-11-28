import scrapy
from whiskyscraper.items import WhiskyscraperItem
from scrapy.loader import ItemLoader


class MezcalSpider(scrapy.Spider):
    name = 'mezcal2'
    start_urls = ['https://www.oldtowntequila.com/mezcal/']

    def parse(self, response):
        for products in response.css('article.card'):
            l = ItemLoader(item = WhiskyscraperItem(), selector=products)

            l.add_css('name', 'p.card-text--brand::text')
            l.add_css('price', 'span.price--main::text')
            l.add_xpath('link', '//*[@id="product-listing-container"]/form/ul/li[8]/article/figure/a/@href')

            yield l.load_item()
        
        next_page = response.css('#product-listing-container > div.pagination > ul > li.pagination-item.pagination-item--next > a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

