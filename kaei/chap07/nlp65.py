#-*- coding: utf-8 -*-

# 参考 : https://www.blog.umentu.work/centos7python3-pymongoの基本的な使い方/

"""
# インタラクティブシェル
$ mongo
> use nlp64_database
> db.nlp64_collection.find({"name":'Queen'})
"""

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# データベースの呼び出し
db = client.nlp64_database

result = db['nlp64_collection'].find({'name':'Queen'})
for r in result:
    print(r)