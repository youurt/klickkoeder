from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


DeclarativeBase = declarative_base()


class Scraping(DeclarativeBase):
    __tablename__ = "heftig"
    news_id = Column('news_id', String(255), primary_key=True)
    headline = Column('headline', String(255))
    img = Column('img', String(255))
    link = Column('link', String(255))
    date = Column('date', String(255))
    scraped_at = Column('scraped_at', DateTime)
