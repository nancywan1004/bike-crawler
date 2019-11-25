import scrapy
from scrapy.loader import ItemLoader
from bike_crawler.items import BikeCrawlerItem

class Bike1Spider(scrapy.Spider):
    name = "bike1_spider"
    start_urls = [
        'https://spokesbicyclerentals.com/collections/cruisers'
    ]

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        for sel in response.xpath("//*[@id='shopify-section-collection-template']/div/div[2]/div[2]/div/div"):
            l = ItemLoader(item=BikeCrawlerItem(), selector = sel)
            l.add_value('site_url', response.url)
            l.add_xpath('bike_name', ".//h3[@class='card__name h4']/text()")
            l.add_xpath('price', ".//div[contains(text(), 'per hour')]/text()")
            item = l.load_item()
        # bike_name = response.xpath("//h3[@class='card__name h4']/text()").extract()
        # price = response.xpath("//*[contains(text(), 'per hour')]/text()")
        # price_normal = price.xpath("normalize-space(.)").extract()
        # site_url = [response.url] * len(bike_name)

        # row_data = zip(bike_name, price)
        # list_row_data = list(row_data)

        #Making extracted data row wise
        # for item in items:
        #     #create a dictionary to store the scraped info
        #     scraped_info = {
        #         #key:value
        #         'page': response.url,
        #         'bike_name' : item[0],
        #         'price' : item[1]
        #     }

        #yield or give the scraped info to scrapy
            yield item