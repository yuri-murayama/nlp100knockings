import redis
import json

def search_tags(name):
    global r2
    tags = r2.lrange(name, 0, -1)
    if tags != []:
        print(tags)
    else:
        print('そのようなアーティストはデータベース内に存在しません')

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
    r2 = redis.StrictRedis(connection_pool=pool)

    with open('artist.json', 'r') as f:
        for line in f:
            artist_info = json.loads(line)
            if 'tags' not in artist_info:
                artist_info['tags'] = 'None'
            r2.rpush(artist_info['name'], artist_info['tags'])

    search_tags('Richard Benson') # >>[b'None', b'None', b'None', b'None']
    search_tags('WIK▲N') # >>[b"[{'count': 1, 'value': 'sillyname'}]"]