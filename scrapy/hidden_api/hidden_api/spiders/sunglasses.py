import scrapy
import json
# https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837?isProductNeeded=true&pageSize=18&responseFormat=json&isChanelCategory=false&currency=USD&gclid=Cj0KCQiA7oyNBhDiARIsADtGRZbSMJvHEKU4O3V91bO7N_f8TWwvVWYvt3VvnFgTcO3KQ6bZTYa4_VQaAtHaEALw_wcB&pageView=image&DM_PersistentCookieCreated=true&categoryId=3074457345626651837&beginIndex=0&cid=PM-SGA_300419-3.US-SGH-EN-NB-Sunglasses_Sunglasses-Men-E_sunglasses+for+men&gclsrc=aw.ds&viewTaskName=CategoryDisplayView&catalogId=20602&langId=-1&storeId=10152&top=Y&orderBy=default&currentPage=3


class SunglassesSpider(scrapy.Spider):
    name = 'sunglasses'
    allowed_domains = ['sunglasseshut.com']
    start_urls = ['https://www.sunglasshut.com/wcs/resources/plp/10152/byCategoryId/3074457345626651837?isProductNeeded=true&pageSize=18&responseFormat=json&isChanelCategory=false&currency=USD&gclid=Cj0KCQiA7oyNBhDiARIsADtGRZbSMJvHEKU4O3V91bO7N_f8TWwvVWYvt3VvnFgTcO3KQ6bZTYa4_VQaAtHaEALw_wcB&pageView=image&DM_PersistentCookieCreated=true&categoryId=3074457345626651837&beginIndex=0&cid=PM-SGA_300419-3.US-SGH-EN-NB-Sunglasses_Sunglasses-Men-E_sunglasses+for+men&gclsrc=aw.ds&viewTaskName=CategoryDisplayView&catalogId=20602&langId=-1&storeId=10152&top=Y&orderBy=default&currentPage=1']

    def parse(self, response):
        data =  json.loads(response.body)
        yield from data['plpView']['products']['products']['product']

        next_page = data['plpView']['nextPageURL']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)