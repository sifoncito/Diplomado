import json
from pymongo import MongoClient
uri = 'mongodb://mongoadmin:secret@localhost:27888/?authSource=admin'
client = MongoClient(uri)

db = client['Diplomado']
collection_name = db['datos']

with open('Analized_Gates.json') as f:
    file_data = json.load(f)

collection_name.insert_one(file_data)

client.close()
