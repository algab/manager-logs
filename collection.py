import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv("./config.env")

def verify_collection():
    client = MongoClient(os.getenv('MONGO_HOST'),27017,username=os.getenv('MONGO_USER'),password=os.getenv('MONGO_PASS'))
    db = client[os.getenv('MONGO_DB')]
    collections = db.list_collection_names()
    if "post_logs" not in collections or "get_logs" not in collections or "put_logs" not in collections or "delete_logs" not in collections:
        if "post_logs" not in collections:
            db.create_collection("post_logs")
        if "get_logs" not in collections:
            db.create_collection("get_logs")
        if "put_logs" not in collections:
            db.create_collection("put_logs")
        if "delete_logs" not in collections:
            db.create_collection("delete_logs")                       