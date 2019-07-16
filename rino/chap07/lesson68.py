# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database

info_list = list(collection.find({'tags.value':'dance'}).sort([('rating.count', -1)]))
for info in info_list[:10]:
    print(info['name'])

"""
========
出力結果
========
Madonna
Björk
The Prodigy
Rihanna
Britney Spears
Maroon 5
Adam Lambert
Fatboy Slim
Basement Jaxx
Cornershop

"""
