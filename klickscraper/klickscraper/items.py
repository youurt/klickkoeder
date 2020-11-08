import scrapy


class HeftigItem(scrapy.Item):

    news_id = scrapy.Field()
    headline = scrapy.Field()
    img = scrapy.Field()
    link = scrapy.Field()
    date = scrapy.Field()
    scraped_at = scrapy.Field()


class WikinewsItem(scrapy.Item):
    page_id = scrapy.Field()
    title = scrapy.Field()
    scraped_at = scrapy.Field()
    category = scrapy.Field()


class BuzzfeedItem(scrapy.Item):
    headline = scrapy.Field()
    scraped_at = scrapy.Field()


class TvMovieItem(scrapy.Item):
    headline = scrapy.Field()
    scraped_at = scrapy.Field()
