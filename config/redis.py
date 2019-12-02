import os
from dotenv import load_dotenv
from redis import Redis

load_dotenv()

cache = Redis(host=os.getenv('REDIS_HOST'))