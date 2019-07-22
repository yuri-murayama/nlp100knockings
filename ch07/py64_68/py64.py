import json
import pymongo

#mongo立ち上げ　mongod --config /usr/local/etc/mongod.conf

def input_data():
    with open('artist.json', 'r', encoding='utf8') as f:
        for line in f:
            i = json.loads(line)
            yield i

def register_data():
    client = pymongo.MongoClient('localhost', 27017)
    db = client['MusicBrainzDb']
    artists = db['artists']

    for lines in input_data():
        artists.insert(lines)

    artists.create_index([('name', pymongo.ASCENDING)])
    artists.create_index([('aliases.name', pymongo.ASCENDING)])
    artists.create_index([('tags.value', pymongo.ASCENDING)])
    artists.create_index([('rating.value', pymongo.ASCENDING)])

if __name__ == '__main__':
    register_data()
