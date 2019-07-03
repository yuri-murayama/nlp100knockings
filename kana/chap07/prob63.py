#-*- coding: utf-8 -*-
#63. オブジェクトを値に格納したKVS

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
			tags = data.get('tags') #タグ

			if tags == None:
				r.rpush(name, 0)
			else:
				tags_count = 0
				for tag in tags:
					tags_count += tag.get('count')
				r.rpush(name, tags_count)	

if __name__ == '__main__':
	get_db('artist.json')

	# 検索したいアーティスト名入力
	print("アーティスト名 > ", end = "")
	name = input()

	# 検索
	for tags_count in r.lrange(name, 0, -1):
		print(tags_count.decode('utf-8'))
