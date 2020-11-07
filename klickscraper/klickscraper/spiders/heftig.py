import scrapy


class HeftigSpider(scrapy.Spider):
    name = 'heftig'
    allowed_domains = ['heftig.de']
    start_urls = ['http://heftig.de/']

    def parse(self, response):
        pass
