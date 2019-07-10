#-*- coding: utf-8 -*-
#68. ソート

from pymongo import MongoClient
from pymongo import ASCENDING, DESCENDING


client = MongoClient('localhost', 27017)

# データベースを作成 (名前: my_database)
db = client.my_database

# コレクションを作成 (名前: my_collection)
co = db.my_collection

# 'dance'をタグにもつアーティストをrating.countで降順にソートしたリストを作成
sorted_dance_artists = list(co.find({'tags.value' : 'dance'}).sort('rating.count', DESCENDING))

for artist in sorted_dance_artists:
	print(artist)