import logging
from scrapy import signals
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from klickscraper.items import HeftigItem
import klickscraper.models as models
import os


class SqlitePipeline:
    def __init__(self, settings):
        self.database = settings.get("DATABASE")
        self.database_dev = settings.get("DATABASE_DEV")
        self.sessions = {}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls(crawler.settings)
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def create_engine(self):
        if "IS_APP_ENGINE" in os.environ:
            # GAE + Cloud SQL
            engine = create_engine(URL(**self.database))
            # GAE + Big Query
            #engine = create_engine("bigquery://regionale-preise/scraping", credentials_path="C:/Users/jwendt/Documents/regionale-preise-96dcb5ae4f68.json")
        else:
            # LOKAL
            engine = create_engine(URL(**self.database_dev))
        return engine

    def create_tables(self, engine):
        models.DeclarativeBase.metadata.create_all(engine, checkfirst=True)

    def create_session(self, engine):
        session = sessionmaker(bind=engine)()
        return session

    def spider_opened(self, spider):
        engine = self.create_engine()
        self.create_tables(engine)
        session = self.create_session(engine)
        self.sessions[spider] = session

    def spider_closed(self, spider):
        session = self.sessions.pop(spider)
        session.close()

    def process_item(self, item, spider):
        session = self.sessions[spider]
        if isinstance(item, HeftigItem):
            scraping_exists = session.query(models.Scraping).filter_by(
                news_id=item["news_id"]).first()
            if scraping_exists is not None:
                s = scraping_exists
            else:
                s = models.Scraping(**{i: item[i] for i in item if i in [
                    "news_id", "headline", "img", "link", "date", "scraped_at"]})

            try:
                session.add(s)
                session.commit()
            except:
                session.rollback()
                raise
            finally:
                session.close()

            return item
