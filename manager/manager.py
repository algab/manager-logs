import json
import time
from database import db
from threading import Thread
from manager.batch import Batch
from manager.file import save_file

config = json.loads(open("config.json").read())

class Manager(Thread):
    def run (self):
        while True:
            self.insert_logs()
            time.sleep(config["time"]) 
                
    def insert_logs(self):
        try:
            inserts = Batch().get_inserts()
            if len(inserts) != 0:
                db[config["collection"]].bulk_write(inserts)
                Batch().reset()     
        except Exception as e:
            save_file(e,"INSERT logs")
            