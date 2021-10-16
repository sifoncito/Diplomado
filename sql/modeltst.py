from pymongo import MongoClient

def getMongo():
    MONGO_HOST= 'mongodb://root:rootpassword@localhost:27017'  # assuming you have mongoDB installed locally
    conn = MongoClient(MONGO_HOST)
    db = conn['historical_Tweets']
    collection = db['BillGates']
    cursor = collection.find({},{"id": 1, "created_at": 1, "full_text": 1, "retweet_count": 1, "favorite_count": 1})
    return cursor


for i in getMongo():
    print(i['created_at'])
    print("\n")