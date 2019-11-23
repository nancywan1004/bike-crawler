import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        # 'https://yescycle.com/bike-rental-vancouver/',
        'https://spokesbicyclerentals.com/collections/cruisers'
    ]

    # def start_requests(self):
    #    start_urls = reversed( [
    #     'https://yescycle.com/bike-rental-vancouver/',
    #     'https://spokesbicyclerentals.com/collections/cruisers'
    #    ] )

    #    return [ Request(url = start_url) for start_url in start_urls ]

    def parse(self, response):
        print("procesing:"+response.url)
        #Extract data using css selectors
        bike_name = response.xpath("//h3[@class='card__name h4']/text()")
        price_num = response.xpath("//*[contains(text(), 'per hour')]/text()").extract()


        row_data = zip(bike_name, price_num)
        list_row_data = list(row_data)

        #Making extracted data row wise
        for item in list_row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                # 'page':response.url,
                'bike_name' : item[0],
                'price_num' : item[1]
            }

        #yield or give the scraped info to scrapy
        yield scraped_info