import json
import pymongo
from bson import ObjectId


def find_name(name):
    client = pymongo.MongoClient('localhost', 27017)
    db = client['MusicBrainzDb']
    artists = db['artists']
    return artists.find({'name':name})

def objectid_str(id):
    # objectid -> json変換必要
    if isinstance(id, ObjectId):
        return str(id)

if __name__ == '__main__':
    for i in find_name('Queen'):
        # iそのまま出力だと見づらい
        data = json.dumps(i, indent=2, sort_keys=True, default=objectid_str)
        print(data)
