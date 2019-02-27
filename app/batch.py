import json
from datetime import datetime
from pymongo import InsertOne
from app.file import save_logs

class Batch(): 
    post_logs = []
    get_logs = []
    put_logs = []
    delete_logs = []         

    def set_inserts(self,doc):
        logs = json.loads(open('./logs.json').read())
        doc["date"] = str(datetime.now())
        logs.append(doc)
        save_logs(logs)          
        doc["date"] = datetime.now()
        if doc["type"] == "POST":
            self.__class__.post_logs.append(InsertOne(doc))
        if doc["type"] == "GET" or doc["type"] == "HEAD":
            self.__class__.get_logs.append(InsertOne(doc))
        if doc["type"] == "PUT" or doc["type"] == "PATCH":
            self.__class__.put_logs.append(InsertOne(doc))
        if doc["type"] == "DELETE":
            self.__class__.delete_logs.append(InsertOne(doc))            
    
    def get_inserts(self):
        return self.__class__.post_logs, self.__class__.get_logs, self.__class__.put_logs, self.__class__.delete_logs 

    def reset(self):
        save_logs([])
        self.__class__.post_logs = []
        self.__class__.get_logs = []
        self.__class__.put_logs = []
        self.__class__.delete_logs = []     