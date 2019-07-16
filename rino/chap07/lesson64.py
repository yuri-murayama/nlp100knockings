# -*- coding: utf-8 -*-

from pymongo import MongoClient
from pymongo import ASCENDING
import json

INPUT_PATH = "./input/artist.json"

client = MongoClient('localhost', 27017)
db = client.artist_database
collection = db.artist_database

length = 921338  # データの件数

with open(INPUT_PATH) as f:
    count = 0
    for line in f:
        if count % 1000 == 0:
            print("{} / {}".format(count, length))

        df = json.loads(line)
        collection.insert_one(df)

        count += 1

collection.create_index([("name", ASCENDING)])
collection.create_index([("aliases.name", ASCENDING)])
collection.create_index([("tags.value", ASCENDING)])
collection.create_index([("rating.value", ASCENDING)])
