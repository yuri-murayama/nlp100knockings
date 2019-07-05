# -*- coding: utf-8 -*-

import plyvel
import json
import pickle

INPUT_PATH = "./input/artist.json"
OUTPUT_DB_PATH = 'lesson63.ldb'

db = plyvel.DB(OUTPUT_DB_PATH, create_if_missing=True)

# データベース構築
with open(INPUT_PATH) as f:
    for line in f:
        df = json.loads(line)

        if 'tags' not in df:
            df['tags'] = ''

        # LevelDBにはリストや辞書はvalueにできないのでpickleでシリアライズする
        df_tags = pickle.dumps(df['tags'])

        db.put(df['name'].encode(), df_tags)

# データベースから検索
a_artist = "Mastodon"
tags_pkl = db.get(a_artist.encode())
tags = pickle.loads(tags_pkl)
print(tags)

"""
========
出力結果
========
[{'count': 3, 'value': 'sludge metal'},
{'count': 3, 'value': 'progressive metal'},
{'count': 2, 'value': 'heavy metal'},
{'count': 1, 'value': 'american'},
{'count': 1, 'value': 'alternative metal'},
{'count': 1, 'value': 'rock and indie'},
{'count': 1, 'value': 'groove metal'},
{'count': 2, 'value': 'metal'}]

"""
