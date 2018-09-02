import json
from manager.batch import Batch
from manager.file import save_file
from flask_expects_json import expects_json
from flask import Blueprint, request, jsonify

log = Blueprint('log',__name__)

model = {
    "type":"object",
    "properties": {
        "type":{"type":"string"},
        "action":{"type":"string"}
    },
    "required":["type","action"]
}

@log.route("/logs",methods=["POST"])
@expects_json(model)
def insert_log():
    try:
        data = request.get_json()
        Batch().set_inserts(data)
        return jsonify({'Message':'Operation Successful'}), 200        
    except Exception as e:
        save_file(e,"POST /logs")
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs",methods=["GET"])
def list_log():
    try:
        logs = json.loads(open("./manager/logs.json").read())
        return jsonify(logs), 200
    except Exception as e:
        save_file(e,"GET /logs")
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs/error",methods=["GET"])
def list_log_error():
    try:
        file_error = open("./manager/error.txt","r")
        content = file_error.readlines()
        file_error.close()
        doc_json = []
        for i,msg in enumerate(content):
            if i == len(content) - 1:
                doc_json.append({'msg':msg})
            else:
                doc_json.append({'msg':msg[0:-1]})            
        content = None    
        return jsonify(doc_json), 200
    except Exception as e:
        save_file(e,"GET /logs/error")
        return jsonify({'Message':'Server Error'}), 500    