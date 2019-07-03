#-*- coding: utf-8 -*-

import json
import leveldb

save_db = leveldb.LevelDB('60.ldb') # [*id, area]
id_db = leveldb.LevelDB('60-id') # [*id, name]

while(1):
    print("アーティスト名を入力してください > ", end="")
    name = input()
    if name=='quit':
        break

    id = []
    for key, value in id_db.RangeIter():
        if value.decode()==name:
            id.append(key)

    for i in id:
        area = save_db.Get(i)
        print(i.decode()+' : '+area.decode())