#-*- coding: utf-8 -*-
#65. MongoDBの検索

import json
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

#サーバー立ち上げ:sudo mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb.log

# インタラクティブシェル
#$ brew services start mongodb
#$ mongo
#$ > use my_database;
#$ > db.my_collection.find({"name":"Queen"})

client = MongoClient('localhost', 27017)

# データベースを作成 (名前: my_database)
db = client.my_database

# コレクションを作成 (名前: my_collection)
co = db.my_collection

# Queenを検索
answer_list = list(co.find({'name': 'Queen'}))
for answer in answer_list:
	print(answer)