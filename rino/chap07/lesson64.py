# -*- coding: utf-8 -*-

from pymongo import MongoClient
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

        if 'aliases' not in df:
            df['aliases'] = [{'name':''}]

        if 'tags' not in df:
            df['tags'] = [{'value':''}]

        if 'rating' not in df:
            df['rating'] = {'value':''}

        post = {'name' : df['name'],
                'aliases_name' : [a['name'] for a in df['aliases']],
                'tags_value' : [t['value'] for t in df['tags']],
                'rating_value' : df['rating']['value']
            }

        collection.insert_one(post)

        count += 1
