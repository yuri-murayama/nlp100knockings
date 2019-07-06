#-*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo import DESCENDING

client = MongoClient('localhost', 27017)

# データベースの呼び出し
db = client.nlp64_database

result = db['nlp64_collection'].find({'tags.value':'dance'})

result.sort('rating.count', DESCENDING)

for r in result.limit(10):
    if 'rating' in r:
        print('{0} : {1}回'.format(r['name'], r['rating']['count']))