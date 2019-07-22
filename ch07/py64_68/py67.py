import json
import pymongo
from bson import ObjectId

def objectid_str(id):
    # objectid -> json変換必要
    if isinstance(id, ObjectId):
        return str(id)

def alias_name(alias):
    # aliases.nameが別名
    client = pymongo.MongoClient('localhost', 27017)
    db = client['MusicBrainzDb']
    artists = db['artists']
    return artists.find({'aliases.name':alias})

if __name__ == '__main__':
    alias = input('Please input artist name. >>> ')
    for i in alias_name(alias):
        data = json.dumps(i, indent=2, sort_keys=True, default=objectid_str)
        print(data)
