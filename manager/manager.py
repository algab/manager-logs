import json
import time
from database import db
from threading import Thread
from datetime import datetime

class Manager(Thread):
    def run (self):
        while True:
            self.insert_logs()
            time.sleep(3600)

    def insert_logs(self):
        try:
            logs = json.loads(open("./manager/logs.json").read())
            if len(logs) != 0:
                db["teste"].insert_many(logs)
                file = open("./manager/logs.json","w")
                json.dump([],file)
                file.close()
        except Exception as e:
            file_error = open("./manager/error.txt","r")
            content = file_error.readlines()
            file_error.close()
            if content:
                info = "\n" + str(datetime.now()) + " - " + str(e)            
            else:
                info = str(datetime.now()) + " - " + str(e)
            content.append(info)
            save_file_error = open("./manager/error.txt","w")
            save_file_error.writelines(content)
            save_file_error.close()