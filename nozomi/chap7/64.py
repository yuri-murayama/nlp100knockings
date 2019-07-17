# -*- coding: utf-8 -*-
import json
from pymongo import MongoClient

client = MongoClient()
db = client.artist_database
collection = db.artist_collection

with open('artist.json','r') as f:
    lst=[]
    for l in f:
        t = json.loads(l)
        lst.append(t)

#print(lst)
result = collection.insert_many(lst)
#print(collection.find_one())
collection.create_index('name')
collection.create_index('aliases.name')
collection.create_index('tags.value')
collection.create_index('rating.value')

print(collection.find_one())
