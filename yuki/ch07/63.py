import json
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r2 = redis.StrictRedis(connection_pool=pool)

def search(r2,artist):
    tags = r2.lrange(artist,0,-1)
    if tags != None:
        return tags
    else:
        return 'None'

with open('artist.json','r') as f:
    for line in f:
        line = json.loads(line)
        if 'tags' in line:
            r2.rpush(line['name'],line['tags'])
        else:
            r2.rpush(line['name'],'None')

print('アーティスト名 : ',end = "")
artist = input()
print(search(r2,artist))
