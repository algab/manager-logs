import json
from manager.manager import Manager
from flask_expects_json import expects_json
from flask import Blueprint, request, jsonify

log = Blueprint('log',__name__)

model = {
    "type":"object",
    "properties": {
        "type":{"type":"string"},
        "action":{"type":"string"},
        "date":{"type":"number","format":"integer"}
    },
    "required":["type","action","date"]
}

@log.route("/logs",methods=["POST"])
@expects_json(model)
def insert_log():
    try:
        data = request.get_json()
        logs = json.loads(open("./manager/logs.json").read())
        logs.append(data)
        file = open("./manager/logs.json","w")
        json.dump(logs,file)
        logs = None
        file.close()
        return jsonify({'Message':'Operation Successful'}),200        
    except Exception as e:
        Manager().save_file(e)
        return jsonify({'Message':'Server Error'}),500

@log.route("/logs/error",methods=["GET"])
def list_log_error():
    try:
        file_error = open("./manager/error.txt","r")
        content = file_error.readlines()
        file_error.close()
        doc_json = []
        for msg in content:
            doc_json.append({'msg':msg[0:-1]})
        content = None    
        return jsonify(doc_json),200
    except Exception as e:
        Manager().save_file(e)
        return jsonify({'Message':'Server Error'}),500    