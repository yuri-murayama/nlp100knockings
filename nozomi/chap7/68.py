# -*- coding: utf-8 -*-
from pymongo import MongoClient

client = MongoClient()
db = client.artist_database
collection = db.artist_collection

dict={}
for ls in collection.find({'tags.value': 'dance'}):
    #print(ls)
    num=ls.get('rating')
    if num !=None:
        num0=num['count']
        #print(num0)
        dict[num0]=ls

#print(dict)
a = sorted(dict.items(), reverse=True, key=lambda x: x[0])[0:10]
#print(a)
print('<<artist top10>>\n')
for a0 in a:
    #print(a0[1])
    print(a0[1]['name'])
