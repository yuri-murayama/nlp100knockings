#-*- coding: utf-8 -*-
#60. KVSの構築

import redis
import json

# Redisに接続　コネクションプールを使う
pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

def get_db(filename):
	
	# jsonファイルを読み込む
	with open(filename) as f:
		for line in f:
			data = json.loads(line)
			name = data.get('name') #名前
			area = data.get('area') #活動地域

			if area != None:
				r.rpush(name, area)
			else:
				r.rpush(name, "no-info")		

if __name__ == '__main__':
	get_db('artist.json')