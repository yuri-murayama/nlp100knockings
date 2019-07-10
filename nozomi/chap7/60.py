# -*- coding: utf-8 -*-

import json
import redis

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

with open('artist.json','r') as f:
    for l in f:
        t = json.loads(l)
        t2 = t['name']
        t3=t.get('area')
        if t3 != None:
            r.rpush(t2,t3)
        else:
            r.rpush(t2,'None')
