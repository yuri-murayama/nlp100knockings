import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['MusicBrainzDb']
artists = db['artists']
country = artists.find({'area':'Japan'})
count = country.count()
print(count)
#49886
