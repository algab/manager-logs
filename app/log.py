import json
import datetime
from database import db
from app.batch import Batch
from app.file import save_error
from validate import validate_request
from flask import Blueprint, request, jsonify

log = Blueprint('log',__name__)

schema = {
    "type":"object",
    "properties": {
        "type":{"type":"string","enum":["POST","PUT","GET","DELETE","PATCH","HEAD"]},
        "action":{"type":"string"}
    },
    "required":["type","action"]
}

@log.route("/logs",methods=["POST"])
@validate_request(schema)
def insert_log():
    try:
        data = request.get_json()
        Batch().set_inserts(data)
        return jsonify({'Message':'Operation Successful'}), 200        
    except Exception as e:
        save_error(e,"POST /logs")
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs",methods=["GET"])
def list_log():
    try:
        data = {}
        logs = json.loads(open("./logs.json").read())
        data["total"] = len(logs)
        data["logs"] = logs
        logs = None
        return jsonify(data), 200
    except Exception as e:
        save_error(e,"GET /logs")
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs/post",methods=["GET"])
def post_logs():
    try:
        docs = []
        action = request.args.get('action')
        time = request.args.get('time')
        if action and time:
            if time == "week" or time == "month" or time == "year":
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db['post_logs'].find({'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    doc["time"] = doc["date"].strftime("%H:%M:%S")
                    doc["date"] = doc["date"].strftime("%d/%m/%Y")
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string action and time are required'}), 400           
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500

@log.route("/logs/get",methods=["GET"])
def get_logs():
    try:
        docs = []
        action = request.args.get('action')
        time = request.args.get('time')
        if action and time:
            if time == "week" or time == "month" or time == "year":
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db['get_logs'].find({'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    doc["time"] = doc["date"].strftime("%H:%M:%S")
                    doc["date"] = doc["date"].strftime("%d/%m/%Y")
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string action and time are required'}), 400           
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500        

@log.route("/logs/put",methods=["GET"])
def put_logs():
    try:
        docs = []
        action = request.args.get('action')
        time = request.args.get('time')
        if action and time:
            if time == "week" or time == "month" or time == "year":
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db['put_logs'].find({'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    doc["time"] = doc["date"].strftime("%H:%M:%S")
                    doc["date"] = doc["date"].strftime("%d/%m/%Y")
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string action and time are required'}), 400           
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500  

@log.route("/logs/delete",methods=["GET"])
def delete_logs():
    try:
        docs = []
        action = request.args.get('action')
        time = request.args.get('time')
        if action and time:
            if time == "week" or time == "month" or time == "year":
                if time == "week":
                    start_delta = datetime.timedelta(days=7)
                elif time == "month":
                    start_delta = datetime.timedelta(days=30)
                elif time == "year":
                    start_delta = datetime.timedelta(days=365)                     
                start = datetime.datetime.now()
                end = start - start_delta
                cursor = db['delete_logs'].find({'action':{'$eq':action},'date':{'$lt':start,'$gt':end}})
                for doc in cursor:
                    doc["_id"] = str(doc["_id"])
                    doc["time"] = doc["date"].strftime("%H:%M:%S")
                    doc["date"] = doc["date"].strftime("%d/%m/%Y")
                    docs.append(doc)    
                return jsonify(docs), 200
            else:
                return jsonify({'Message':'Query string time are week, month or year'}), 400     
        else:
            return jsonify({'Message':'Query string action and time are required'}), 400           
    except Exception as e:
        return jsonify({'Message':'Server Error'}), 500                    
                    
@log.route("/logs/error",methods=["GET"])
def list_log_error():
    try:
        file_error = open("./error.txt","r")
        content = file_error.readlines()
        file_error.close()
        doc_json = []
        for i,msg in enumerate(content):
            if i == len(content) - 1:
                doc_json.append({'Message':msg})
            else:
                doc_json.append({'Message':msg[0:-1]})            
        content = None    
        return jsonify(doc_json), 200
    except Exception as e:
        save_error(e,"GET /logs/error")
        return jsonify({'Message':'Server Error'}), 500    