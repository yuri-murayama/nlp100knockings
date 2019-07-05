# -*- coding: utf-8 -*-

import plyvel

OUTPUT_DB_PATH = 'lesson60.ldb'

db = plyvel.DB(OUTPUT_DB_PATH, create_if_missing=True)

count = 0
for artist, area in db:
    if area == b"Japan":
        count += 1

print(count)

"""
========
出力結果
========

21946

"""
