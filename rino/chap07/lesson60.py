# -*- coding: utf-8 -*-

import plyvel
import json

INPUT_PATH = "./input/artist.json"
OUTPUT_DB_PATH = 'lesson60.ldb'
db = plyvel.DB(OUTPUT_DB_PATH, create_if_missing=True)

with open(INPUT_PATH) as f:
    for line in f:
        df = json.loads(line)

        if 'area' not in df:
            df['area'] = ''

        db.put(df['name'].encode(), df['area'].encode())
