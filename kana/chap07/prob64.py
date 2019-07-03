#-*- coding: utf-8 -*-
#64. MongoDBの構築

import json
from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING

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
	
print(co.find_one())

# indexを付与
#db.collection.createIndex( { name: 1, aliases.name:1, tags.value:1, rating.value:1 } )
