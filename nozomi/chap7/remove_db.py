from pymongo import MongoClient

client = MongoClient()
db = client.artist_database
collection = db.artist_collection

client.drop_database(db)
