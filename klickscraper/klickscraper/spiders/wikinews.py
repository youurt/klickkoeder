import scrapy
from scrapy import Request
import json
from datetime import datetime
from klickscraper.items import WikinewsItem


class WikinewsSpider(scrapy.Spider):
    name = 'wikinews'

    def __init__(self, cat=None, *args, **kwargs):
        self.cat = cat

    # categories = ['Themenportal_Politik',
    #               'Themenportal_Wirtschaft', 'Themenportal_Kultur', 'Themenportal_Unfall', 'Themenportal_Wetter', 'Themenportal_Sport', 'Themenportal_Arbeit_und_Soziales', 'Themenportal_Umwelt', 'Themenportal_Computer', 'Themenportal_Wissenschaft', 'Themenportal_Recht']
    scraped_at = datetime.now()

    def start_requests(self):
        yield Request(
            url=f'https://de.wikinews.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{self.cat}&format=json&cmlimit=max',
            dont_filter=True)

    def parse(self, response):
        results = json.loads(response.body)
        articles = results['query']['categorymembers']

        for article in articles:
            yield WikinewsItem(
                page_id=article['pageid'],
                title=article['title'],
                scraped_at=self.scraped_at,
                category=self.cat
            )

        if "continue" in results:
            cont = results['continue'].get('cmcontinue')

            yield Request(
                url=f'https://de.wikinews.org/w/api.php?action=query&list=categorymembers&cmtitle=Category:{self.cat}&format=json&cmlimit=max&cmcontinue={cont}',
                dont_filter=True,
                callback=self.parse
            )
        else:
            return
