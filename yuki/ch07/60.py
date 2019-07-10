import json
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

with open('artist.json','r') as f:
    for line in f:
        line = json.loads(line)
        if 'area' in line:
            r.rpush(line['name'],line['area'])
        else:
            r.rpush(line['name'],'None')
