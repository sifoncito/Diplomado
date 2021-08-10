import pymongo
uri = 'mongodb://mongoadmin:secret@localhost:27888/?authSource=admin'
client = pymongo.MongoClient(uri)

db = client['Diplomado']
collection_name = db['datos']

x = []
date = collection_name.find({}, {"created_at"})
for i in date:
    x.append(i)
print(x)

