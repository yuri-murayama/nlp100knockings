#-*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)

# データベースの呼び出し
db = client.nlp64_database

while(1):
    print("アーティスト別名を入力してください > ", end="")
    aliases = input()

    if aliases=='quit':
        break

    result = db['nlp64_collection'].find({'aliases.name':aliases})
    for r in result:
        print(r)