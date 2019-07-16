# -*- coding: utf-8 -*-

'''
インタラクティブシェル

> use artist_database
switched to db artist_database

> db.artist_database.find({'area':'Japan'}).count()
22821

'''

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database

count = 0
for info in collection.find({'area':'Japan'}):
    count += 1

print(count)

"""
========
出力結果
========
22821

"""
