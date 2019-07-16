# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database

artist_name = input() # アーティストの別名を入力
for info in collection.find({'aliases.name':artist_name}):
    print(info)
