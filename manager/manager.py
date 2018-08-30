import json
import time
from database import db
from threading import Thread
from manager.file import save_file

class Manager(Thread):
    def run (self):
        while True:
            self.insert_logs()
            time.sleep(60) 
                
    def insert_logs(self):
        try:
            config = json.loads(open("config.json").read())
            logs = json.loads(open("./manager/logs.json").read())
            if len(logs) != 0:
                db[config["collection"]].insert_many(logs)
                file = open("./manager/logs.json","w")
                json.dump([],file)
                logs = None
                file.close()
        except Exception as e:
            save_file(e,"INSERT logs")
            