# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

counter = 0
for name in r.keys():
    if b'Japan' in r.lrange(name,0,-1):
            counter+=1
print('該当件数：{}件'.format(counter))
