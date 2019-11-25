# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from bike_crawler.items import BikeCrawlerItem

class Bike2Spider(scrapy.Spider):
    name = 'bike2_spider'
    start_urls = ['https://www.englishbaybikerentals.com/rental-bikes']

    def parse(self, response):
        print("procesing:"+response.url)

        for sel in response.xpath("//*[@id='comp-imfikiyx_NewsPostsView_i7ezjf6w56_dup_i7g5gc7h79_imfikizg_Array__0_0_paginatedlistinlineContent']/div"):
            l = ItemLoader(item=BikeCrawlerItem(), selector = sel)
            l.add_value('site_url', response.url)
            l.add_xpath('bike_name', ".//div//p/strong/em/strike/u/text()")
            l.add_xpath('price', ".//span[contains(text(), '1 HR')]/text()")
            item = l.load_item()
        #Extract data using css selectors
        # bike_name = response.xpath("//div//p/strong/em/strike/u/text()").extract()
        # price = response.xpath("//span[contains(text(), '1 HR')]/text()").extract()
        # site_url = [response.url] * len(bike_name)

        # row_data = zip(site_url, bike_name, price)
        # list_row_data = list(row_data)

        #Making extracted data row wise
        # for item in list_row_data:
        #     #create a dictionary to store the scraped info
        #     scraped_info = {
        #         #key:value
        #         'page': item[0],
        #         'bike_name' : item[1],
        #         'price' : item[2]
        #     }

            #yield or give the scraped info to scrapy
            yield item

