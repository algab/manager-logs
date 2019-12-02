import os
import json
import time
from threading import Thread
from datetime import datetime
from pymongo import InsertOne
from config.database import db
from config.redis import cache

class Schedule(Thread):
    def run(self):
        while True:
            self.save_logs()
            time.sleep(int(os.getenv('TIME_SECONDS')))

    def save_logs(self):
        try:
            data = cache.get('logs')
            if data != None:
                insert_logs = []
                data = json.loads(data)
                for log in data:
                    log['date'] = datetime.strptime(log['date'], '%Y-%m-%d %H:%M:%S.%f')
                    insert_logs.append(InsertOne(log))
                db[os.getenv('MONGO_COLLECTION')].bulk_write(insert_logs)
                cache.delete('logs')
        except Exception as e:
            print(e)
