# -*- coding: utf-8 -*-

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database

for info in collection.find({'name':'Queen'}):
    print(info)

"""
========
出力結果
========

{'_id': ObjectId('5d1c581f557ba310d3489708'), 'name': 'Queen', 'aliases_name': ['Queen'], 'tags_value': ['kamen rider w', 'related-akb48'], 'rating_value': ''}
{'_id': ObjectId('5d1c587f557ba310d3495db4'), 'name': 'Queen', 'aliases_name': ['女王'], 'tags_value': ['hard rock', '70s', 'queen family', '90s', '80s', 'glam rock', 'british', 'english', 'uk', 'pop/rock', 'pop-rock', 'britannique', 'classic pop and rock', 'queen', 'united kingdom', 'langham 1 studio bbc', 'kind of magic', 'band', 'rock', 'platinum'], 'rating_value': 92}
...

"""
