import scrapy
from scrapy import Request
from klickscraper.items import TvMovieItem
from datetime import datetime


class TvmovieSpider(scrapy.Spider):
    name = 'tvmovie'
    allowed_domains = ['www.tvmovie.de']
    start_urls = ['http://www.tvmovie.de/news']
    scraped_at = datetime.now()

    def start_requests(self):
        for i in range(700):
            yield Request(
                url=f'https://www.tvmovie.de/news?page={i}',
                dont_filter=True
            )

    def parse(self, response):

        titles = response.css('.headline::text').getall()
        for title in titles:

            yield TvMovieItem(
                headline=title,
                scraped_at=self.scraped_at
            )
