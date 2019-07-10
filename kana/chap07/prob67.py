#-*- coding: utf-8 -*-
#67. 複数のドキュメントの取得

from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING


client = MongoClient('localhost', 27017)

# データベースを作成 (名前: my_database)
db = client.my_database

# コレクションを作成 (名前: my_collection)
co = db.my_collection


# 検索したいアーティスト名入力
print("アーティスト名 > ", end = "")
name = input()

# その名前を別名に持つアーティストのidを検索
print(list(co.find({'aliases.name': name})))

