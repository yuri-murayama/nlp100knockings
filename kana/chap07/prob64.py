#-*- coding: utf-8 -*-
#64. MongoDBの構築

import json
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

#サーバー立ち上げ:sudo mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb.log

client = MongoClient('localhost', 27017)

# データベースを作成 (名前: my_database)
db = client.my_database

# コレクションを作成 (名前: my_collection)
co = db.my_collection


# jsonファイルを読み込み、ドキュメントを格納
with open('artist.json') as f:
	for line in f:	
		df = json.loads(line)
		co.insert_one(df)

# indexを付与
print(co)
co.create_index([("name", ASCENDING)])
co.create_index([("aliases.name", ASCENDING)])
co.create_index([("tags.value", ASCENDING)])
co.create_index([("rating.value", ASCENDING)])
