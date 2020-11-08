from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


DeclarativeBase = declarative_base()


class Heftig(DeclarativeBase):
    __tablename__ = "heftig"
    news_id = Column('news_id', String(255), primary_key=True)
    headline = Column('headline', String(255))
    img = Column('img', String(255))
    link = Column('link', String(255))
    date = Column('date', String(255))
    scraped_at = Column('scraped_at', DateTime)


class Wiki(DeclarativeBase):
    __tablename__ = "wiki"
    page_id = Column('page_id', String(255), primary_key=True)
    title = Column("title", String(255))
    category = Column("category", String(255))
    scraped_at = Column('scraped_at', DateTime)


class Buzz(DeclarativeBase):
    __tablename__ = "buzz"
    id = Column(Integer, primary_key=True)
    headline = Column("headline", String(255))
    scraped_at = Column('scraped_at', DateTime)


class Tvmovie(DeclarativeBase):
    __tablename__ = "tvmovie"
    id = Column(Integer, primary_key=True)
    headline = Column("headline", String(255))
    scraped_at = Column('scraped_at', DateTime)
