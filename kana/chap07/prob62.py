#-*- coding: utf-8 -*-
#62. KVS内の反復処理

import redis

# Redisに接続　コネクションプールを使う
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# 全アーティストを検索してvalueのリストにJapanを含む名前を出力
for name in r.keys():
	if b'Japan' in r.lrange(name, 0, -1):
		print (name.decode('utf-8'))