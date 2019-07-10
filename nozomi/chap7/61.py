# -*- coding: utf-8 -*-
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

def area_search(name):
    for area in r.lrange(name,0,-1):
        print(area.decode('utf-8'))

key = input('artist>> ')
area_search(key)
