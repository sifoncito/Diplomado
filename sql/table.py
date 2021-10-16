### models.py ###

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy import create_engine

DATABASE_URI = 'postgresql://postgres:password@172.18.0.3:5432/tweets'

engine = create_engine(DATABASE_URI)
Base = declarative_base()

class Book(Base):
    __tablename__ = 'pops'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    
    def __repr__(self):
        return "<Book(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)


Base.metadata.create_all(engine)