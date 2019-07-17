import json
from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist


with open('artist.json','r') as f:
    for line in f:
        line = json.loads(line)
        collection.insert_one(line)

# print(collection)
collection.create_index('name')
collection.create_index('aliased.name')
collection.create_index('tags.value')
collection.create_index('rating.value')
print(collection.find_one())
