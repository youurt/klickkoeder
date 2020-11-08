import scrapy
from scrapy import Request, Selector
import json
from klickscraper.items import BuzzfeedItem
from datetime import datetime


class BuzzfeedSpider(scrapy.Spider):
    name = 'buzzfeed'
    allowed_domains = ['buzzfeed.de']
    start_urls = ['http://buzzfeed.de/']
    scraped_at = datetime.now()

    def start_requests(self):
        for page in range(6):
            yield Request(
                url=f'https://www.buzzfeed.com/de/feedpage/feed/home?page={page}&page_name=home&response_format=json',
                dont_filter=True
            )

    def parse(self, response):

        results = json.loads(response.body)['content']
        atag = Selector(text=results).xpath('//a/text()').extract()
        res = map(str.strip, atag)
        str_list = filter(None, list(res))
        end_list = list(str_list)

        for item in end_list:
            yield BuzzfeedItem(
                headline=item,
                scraped_at=self.scraped_at
            )
