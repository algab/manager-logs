import json
import time
from database import db
from threading import Thread
from datetime import datetime

class Manager(Thread):
    def run (self):
        while True:
            self.insert_logs()
            time.sleep(60)

    def save_file(self,e):
        file_error = open("./manager/error.txt","r")
        content = file_error.readlines()
        file_error.close()
        if content:
            if len(content) < 5:
                info = "\n" + str(datetime.now()) + " - " + str(e)
                content.append(info)
            else:
                info = str(datetime.now()) + " - " + str(e)
                content = []
                content.append(info)
        else:
            info = str(datetime.now()) + " - " + str(e)
            content.append(info)
        save_file_error = open("./manager/error.txt","w")
        save_file_error.writelines(content)
        content = None
        save_file_error.close()            
                
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
            self.save_file(e)
            