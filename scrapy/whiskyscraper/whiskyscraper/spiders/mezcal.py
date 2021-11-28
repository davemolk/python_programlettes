import scrapy

class MezcalSpider(scrapy.Spider):
    name = 'mezcal'
    start_urls = ['https://www.oldtowntequila.com/mezcal/']

    def parse(self, response):
        for products in response.css('article.card'):
            try:
                yield {
                    'name': products.css('p.card-text--brand::text').get(),
                    'price': products.css('span.price--main::text').get(),
                    'link': products.xpath('//*[@id="product-listing-container"]/form/ul/li[8]/article/figure/a').attrib['href'],
                }
            except:
                yield {
                    'name': products.css('p.card-text--brand::text').get(),
                    'price': 'sold out',
                    'link': products.xpath('//*[@id="product-listing-container"]/form/ul/li[8]/article/figure/a').attrib['href'],
                }
        next_page = response.css('#product-listing-container > div.pagination > ul > li.pagination-item.pagination-item--next > a').attrib['href']
        # next_page = response.xpath('//*[@id="product-listing-container"]/div[2]/ul/li[7]/a').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)


#product-listing-container > div.pagination > ul > li.pagination-item.pagination-item--next > a