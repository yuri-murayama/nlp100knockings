from pymongo import MongoClient

client = MongoClient()
db = client.testdb
collection = db.artist

print("アーティスト名 : ",end = "")
artist = input()

print(list(collection.find({"aliases.name":artist})))
