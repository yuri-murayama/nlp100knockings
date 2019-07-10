from pymongo import MongoClient
import json

client = MongoClient()
db = client.artist_db
collection = db.artist_collection

with open('artist.json', 'r') as f:
    block = []
    for i, line in enumerate(f, 1):
        artist_info = json.loads(line)
        block.append(artist_info)
        if i % 5000 == 0:
            collection.insert_many(block)
            block = []
    collection.insert_many(block)

collection.create_index('name')
collection.create_index('aliases.name')
collection.create_index('tags.value')
collection.create_index('rating.value')