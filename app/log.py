import os
import json
import datetime
from app.batch import save_logs
from config.database import db
from config.redis import cache
from config.validate import validate_request
from flask import Blueprint, request, jsonify

log = Blueprint('log',__name__)

schema = {
    "type":"object",
    "properties": {
        "type":{"type":"string"},
        "action":{"type":"string","enum":["INSERT","GET","UPDATE","DELETE"]}
    },
    "required":["type","action"]
}

@log.route("/logs",methods=["POST"])
@validate_request(schema)
def insert_log():
    try:
        data = request.get_json()
        save_logs(data)
        return jsonify({'Message':'Operation Successful'}), 200        
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs",methods=["GET"])
def list_logs():
    try:
        action = request.args.get('action')
        time = request.args.get('time')
        if action and time:
            if time == "week" or time == "month" or time == "year":
                docs = []
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db[os.getenv('MONGO_COLLECTION')].find({'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string action and time are required'}), 400           
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs/now",methods=["GET"])
def list_logs_now():
    try:
        data = cache.get('logs')
        if data == None:
            return jsonify([]), 200
        else:
            logs = json.loads(data)
            return jsonify(logs), 200
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500