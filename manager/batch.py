import json
from datetime import datetime
from pymongo import InsertOne

path = "./manager/logs.json"

class Batch():  

    inserts = []   

    def set_inserts(self,doc):
        log = {}
        for key in doc.keys():
            log[key] = doc[key]
        logs = json.loads(open(path).read())
        doc["date"] = str(datetime.now())
        logs.append(doc)
        file = open(path,"w")
        json.dump(logs,file)
        file.close()
        logs = None    
        log["date"] = datetime.now()
        self.__class__.inserts.append(InsertOne(log))

    def get_inserts(self):
        return self.__class__.inserts    

    def reset(self):
        file = open(path,"w")
        json.dump([],file)
        file.close()
        self.__class__.inserts = []     

