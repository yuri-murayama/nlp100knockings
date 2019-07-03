#-*- coding: utf-8 -*-

import json
import leveldb

save_db = leveldb.LevelDB('60.ldb')

count = 0
for key, value in save_db.RangeIter():
    if value.decode()=='Japan':
        count+=1

print(count) # 22821