import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv('./config.env')

client = MongoClient(os.getenv('MONGO_HOST'),27017,username=os.getenv('MONGO_USER'),password=os.getenv('MONGO_PASS'))

db = client[os.getenv('MONGO_DB')]