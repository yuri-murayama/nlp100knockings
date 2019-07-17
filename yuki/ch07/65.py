from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist


for info in collection.find({'name':'Queen'}):
    print(info)
