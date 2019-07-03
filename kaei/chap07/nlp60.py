#-*- coding: utf-8 -*-

import json
import leveldb

def make_db(path):

    # 保存先
    save_db = leveldb.LevelDB('60.ldb') # [*id, area]
    id_db = leveldb.LevelDB('60-id') # [*id, name]

    with open(path) as f:
        lines = f.readlines()
    
    for line in lines:
        json_dict = json.loads(line)

        id = str(json_dict['id'])
        name = json_dict['name']
        area = json_dict.get('area', '')

        save_db.Put(id.encode('utf-8'), area.encode('utf-8'))
        id_db.Put(id.encode('utf-8'), name.encode('utf-8'))

if __name__=='__main__':
    path = './artist.json'
    make_db(path)

