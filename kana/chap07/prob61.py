#-*- coding: utf-8 -*-
#61. KVSの検索

import redis

# Redisに接続　コネクションプールを使う
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# 検索したいアーティスト名入力
print("アーティスト名 > ", end = "")
name = input()

# データベースからアーティスト名を検索
#　Listを0(最初)から-1(全部)まで照会
for country in r.lrange(name, 0, -1):
	print(country.decode('utf-8'))

