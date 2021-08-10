import pandas as pd 
import nltk 
nltk.download('vader_lexicon')
import json

from nltk.sentiment.vader import SentimentIntensityAnalyzer
sid = SentimentIntensityAnalyzer()

Gates_data = pd.read_csv('cleanedGates.csv')

Gates_data['scores'] = Gates_data['text'].apply(lambda text:
        sid.polarity_scores(str(text)))
Gates_data['compound']  = Gates_data['scores'].apply(lambda score_dict: score_dict['compound'])
Gates_data['comp_score'] = Gates_data['compound'].apply(lambda c: 'pos' if c >=0 else 'neg')

Gates_data.to_json('AnalizedGates.json')
