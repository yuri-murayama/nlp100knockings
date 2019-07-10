from pymongo import MongoClient

client = MongoClient()
db = client.artist_db
collection = db.artist_collection

for post in collection.find({'name': 'Queen'}):
    print(post)

'''
プログラム実行結果
{'type': 'Character', 'tags': [{'count': 1, 'value': 'kamen rider w'}, {'count': 1, 'value': 'related-akb48'}], 'ended': True, 'name': 'Queen', 'sort_name': 'Queen', 'area': 'Japan', 'aliases': [{'sort_name': 'Queen', 'name': 'Queen'}], 'id': 701492, 'gid': '420ca290-76c5-41af-999e-564d7c71f1a7', 'gender': 'Female', '_id': ObjectId('5d21aa7208fd2f5b6dccc5e3')}
{'aliases': [{'sort_name': '女王', 'name': '女王'}], 'gid': '0383dadf-2a4e-4d10-a46a-e9e041da8eb3', 'name': 'Queen', 'area': 'United Kingdom', 'rating': {'count': 24, 'value': 92}, 'type': 'Group', 'tags': [{'count': 2, 'value': 'hard rock'}, {'count': 1, 'value': '70s'}, {'count': 1, 'value': 'queen family'}, {'count': 1, 'value': '90s'}, {'count': 1, 'value': '80s'}, {'count': 1, 'value': 'glam rock'}, {'count': 4, 'value': 'british'}, {'count': 1, 'value': 'english'}, {'count': 2, 'value': 'uk'}, {'count': 1, 'value': 'pop/rock'}, {'count': 1, 'value': 'pop-rock'}, {'count': 1, 'value': 'britannique'}, {'count': 1, 'value': 'classic pop and rock'}, {'count': 1, 'value': 'queen'}, {'count': 1, 'value': 'united kingdom'}, {'count': 1, 'value': 'langham 1 studio bbc'}, {'count': 1, 'value': 'kind of magic'}, {'count': 1, 'value': 'band'}, {'count': 6, 'value': 'rock'}, {'count': 1, 'value': 'platinum'}], 'ended': True, 'sort_name': 'Queen', 'begin': {'year': 1970, 'date': 27, 'month': 6}, 'id': 192, '_id': ObjectId('5d21aa7508fd2f5b6dcd8c8f')}
{'ended': True, 'gid': '5eecaf18-02ec-47af-a4f2-7831db373419', 'sort_name': 'Queen', 'id': 992994, 'name': 'Queen', '_id': ObjectId('5d21aa7c08fd2f5b6dcf46e7')}


インタラクティブシェル検索結果
mongo
use artist_db
db.artist_collection.find({'name': 'Queen'})

{ "_id" : ObjectId("5d21aa7208fd2f5b6dccc5e3"), "ended" : true, "id" : 701492, "type" : "Character", "tags" : [ { "value" : "kamen rider w", "count" : 1 }, { "value" : "related-akb48", "count" : 1 } ], "sort_name" : "Queen", "name" : "Queen", "gender" : "Female", "gid" : "420ca290-76c5-41af-999e-564d7c71f1a7", "area" : "Japan", "aliases" : [ { "name" : "Queen", "sort_name" : "Queen" } ] }
{ "_id" : ObjectId("5d21aa7508fd2f5b6dcd8c8f"), "ended" : true, "rating" : { "value" : 92, "count" : 24 }, "sort_name" : "Queen", "name" : "Queen", "type" : "Group", "begin" : { "month" : 6, "year" : 1970, "date" : 27 }, "id" : 192, "tags" : [ { "value" : "hard rock", "count" : 2 }, { "value" : "70s", "count" : 1 }, { "value" : "queen family", "count" : 1 }, { "value" : "90s", "count" : 1 }, { "value" : "80s", "count" : 1 }, { "value" : "glam rock", "count" : 1 }, { "value" : "british", "count" : 4 }, { "value" : "english", "count" : 1 }, { "value" : "uk", "count" : 2 }, { "value" : "pop/rock", "count" : 1 }, { "value" : "pop-rock", "count" : 1 }, { "value" : "britannique", "count" : 1 }, { "value" : "classic pop and rock", "count" : 1 }, { "value" : "queen", "count" : 1 }, { "value" : "united kingdom", "count" : 1 }, { "value" : "langham 1 studio bbc", "count" : 1 }, { "value" : "kind of magic", "count" : 1 }, { "value" : "band", "count" : 1 }, { "value" : "rock", "count" : 6 }, { "value" : "platinum", "count" : 1 } ], "gid" : "0383dadf-2a4e-4d10-a46a-e9e041da8eb3", "area" : "United Kingdom", "aliases" : [ { "name" : "女王", "sort_name" : "女王" } ] }
{ "_id" : ObjectId("5d21aa7c08fd2f5b6dcf46e7"), "ended" : true, "id" : 992994, "gid" : "5eecaf18-02ec-47af-a4f2-7831db373419", "sort_name" : "Queen", "name" : "Queen" }
'''