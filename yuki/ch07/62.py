import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
counter = 0
for artist in r.keys():
    area = r.lrange(artist,0,-1)
    if b'Japan' in area:
        counter += 1
print(counter)

#22554
