# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient()
db = client.artist_database
collection = db.artist_collection

for ls in collection.find({'aliases.name': 'Queen'}):
    print(ls)
