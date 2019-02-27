import json
from datetime import datetime

path_logs = "./logs.json"
path_error = "./error.txt"

def save_logs(logs):
    file_logs = open(path_logs,"w")
    json.dump(logs,file_logs)
    file_logs.close()

def save_error(e,action):
    file_error = open(path_error,"r")
    content = file_error.readlines()
    file_error.close()
    if content:
        if len(content) < 10:
            info = "\n" + str(datetime.now()) + " - " + action + " - " + str(e)
            content.append(info)
        else:
            info = str(datetime.now()) + " - " + action + " - " + str(e)
            content = []
            content.append(info)
    else:
        info = str(datetime.now()) + " - " + action + " - " + str(e)
        content.append(info)
    save_file_error = open(path_error,"w")
    save_file_error.writelines(content)
    save_file_error.close()
    content = None  