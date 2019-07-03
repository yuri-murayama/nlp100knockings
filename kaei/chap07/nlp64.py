#-*- coding: utf-8 -*-

# 参考 : https://qiita.com/ognek/items/a37dd1cd0e26e6adecaa

# connection refusedのエラー対処
# brew services star mongodb (参考 : https://www.maytry.net/mac-mongo-reason-errno-61-connection-refused/)

from pymongo import MongoClient
from pymongo import ASCENDING
import json

client = MongoClient('localhost', 27017)

# データベースの呼び出し
db = client.nlp64_database

# コレクションの呼び出し
collection = db.nlp64_collection

path = './artist.json'
with open(path) as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    result = collection.insert_one(json.loads(line))

    if i%1000==0:
        print(str(i)+" / "+str(len(lines)))

collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
