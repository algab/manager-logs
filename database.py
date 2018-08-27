import json
from pymongo import MongoClient

config = json.loads(open("config.json").read())

client = MongoClient(config["host"],27017,username=config["username"],password=config["password"])

db = client[config["database"]]