import json
import pymongo
from bson import ObjectId

def count_dance():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['MusicBrainzDb']
    artists = db['artists']
    # 曲の分類は、tagの中のvalueに書いてある　death metalとかもある
    dance_tag = artists.find({'tags.value':'dance'})
    dance_sort = dance_tag.sort('rating.count', pymongo.DESCENDING)
    return dance_sort

if __name__ == '__main__':
    # 上位10人出力
    for i in count_dance()[0:10]:
        print('{}\t{}'.format(i['name'], i['rating']['count']))
