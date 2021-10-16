from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, REAL, Boolean, create_engine
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from modeltst import getMongo

### config.py ###
# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
DATABASE_URI = 'postgresql://postgres:password@172.18.0.2:5432/tweets'

engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
s = Session()

class HistoricalTweets(Base):
    __tablename__ = 'tweets'
    id = Column(Integer, primary_key=True)
    published = Column(Date)
    tweet = Column(String)
    favorite = Column(Integer)
    retweets = Column(Integer)
    
    def __repr__(self):
        return "<HistoricalTweets(published={}, tweet='{}', favorite={}, retweets={})>"\
                .format(self.published, self.tweet, self.favorite, self.retweets)


#eltweet = HistoricalTweets(
#    published = datetime(1992, 12, 1),
#    tweet = 'Este es el tweet prrro',
#    favorite = 13,
#    retweets = 16,
#)

Base.metadata.create_all(engine)

#s.add(eltweet)
#s.commit()


def Basecommit():
    for i in getMongo():
        eltweet = HistoricalTweets(
        published = i['created_at'],
        tweet = i['full_text'],
        favorite = i['favorite_count'],
        retweets = i['retweet_count']
        )        
        s.add(eltweet)    
        s.commit()

Basecommit()
