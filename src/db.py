from pymongo import MongoClient


db = None
try:
    client = MongoClient("mongodb://mongo/")
    db = client.musicaDB
except Exception as e:
    print(e)
