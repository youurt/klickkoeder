import scrapy


class HeftigItem(scrapy.Item):

    news_id = scrapy.Field()
    headline = scrapy.Field()
    img = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    scraped_at = scrapy.Field()
