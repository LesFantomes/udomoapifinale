from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class mangaSchema(Base):
    __tablename__ = 'mangas2'

    idManga = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    editor = Column(String)
