#-*- coding: utf-8 -*-

# 参考 : https://qiita.com/tomotaka_ito/items/60c65dd5261fdfc6e71a#leveldbとは

import json
import leveldb
import pickle

def make_db(path):

    with open(path) as f:
        lines = f.readlines()
    
    for line in lines:
        json_dict = json.loads(line)

        id = str(json_dict['id'])
        name = json_dict['name']
        tags = json_dict.get('tags', '')
        serialized = pickle.dumps(tags)

        save_db.Put(id.encode('utf-8'), serialized)
        id_db.Put(id.encode('utf-8'), name.encode('utf-8'))
    
if __name__=='__main__':
    # 保存先
    save_db = leveldb.LevelDB('63.ldb') # [*id, area]
    id_db = leveldb.LevelDB('63-id') # [*id, name]

    # DBの構築
    path = './artist.json'
    #make_db(path)
    print("DBの構築が完了しました")

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
            print(i.decode())

            tags = pickle.loads(save_db.Get(i))
            for t in tags:
                print(t['value'], str(t['count'])+"回")
            print()
