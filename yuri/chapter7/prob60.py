import redis
import json

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

with open('artist.json', 'r') as f:
    for line in f:
        artist_info = json.loads(line)
        if 'area' not in artist_info:
            artist_info['area'] = 'None'
        r.rpush(artist_info['name'], artist_info['area']) # Lists型