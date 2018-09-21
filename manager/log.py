import json
import datetime
from database import db
from manager.batch import Batch
from manager.file import save_file
from flask_expects_json import expects_json
from flask import Blueprint, request, jsonify

config = json.loads(open("config.json").read())

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
        data = {}
        logs = json.loads(open("./manager/logs.json").read())
        data["total"] = len(logs)
        data["logs"] = logs
        logs = None
        return jsonify(data), 200
    except Exception as e:
        save_file(e,"GET /logs")
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs/stats",methods=["GET"])
def stats():
    try:
        docs = []
        type_logs = request.args.get('type')
        action = request.args.get('action')
        time = request.args.get('time')
        if type_logs and action and time:
            if time == "week" or time == "month" or time == "year":
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db[config['collection']].find({'type':{'$eq':type_logs},'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    doc["date"] = int(doc["date"].strftime("%s")) * 1000
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string type, action and time are required'}), 400           
    except Exception as e:
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