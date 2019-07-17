from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist


top_artist = {}
for info in collection.find({'tags.value':'dance'}):
    rating = info.get('rating')
    if rating != None:
        top_artist[info.get('name')] = rating['count']

sorted_top_artist = sorted(top_artist.items(), key = lambda x:x[1],reverse = True)

for artist in sorted_top_artist[0:10]:
    print(artist)
