import scrapy
from scrapy import Request
import json
from klickscraper.items import HeftigItem
from datetime import datetime
from urllib.parse import urlparse


class HeftigSpider(scrapy.Spider):
    name = 'heftig'
    allowed_domains = ['heftig.de']
    start_urls = ['http://heftig.de/']
    scraped_at = datetime.now()

    def start_requests(self):
        for page in range(9):
            yield Request(
                url=f'https://www.heftig.de/_main_json/{page}.json',
                dont_filter=True
            )

    def parse(self, response):
        results = json.loads(response.body)
        feed_list = results["feed"]
        for feed_element in feed_list:
            yield HeftigItem(
                news_id=feed_element['id'],
                headline=feed_element['headline'],
                img=feed_element['img'],
                link=feed_element['link'],
                date=feed_element['date'],
                scraped_at=self.scraped_at
            )
