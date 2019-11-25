import csv
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

from spiders.bike1_spider import Bike1Spider
from spiders.bike2_spider import Bike2Spider


configure_logging()
runner = CrawlerRunner(settings={
    'FEED_FORMAT': 'csv',
    'FEED_URI': 'bikecrawler.csv'
})

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(Bike1Spider)
    yield runner.crawl(Bike2Spider)
    reactor.stop()

crawl()
reactor.run() # the script will block here until the last crawl call is finished