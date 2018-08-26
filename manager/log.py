import json
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
        logs = json.loads(open("./manager/logs.json").read())
        logs.append(data)
        file = open("./manager/logs.json","w")
        json.dump(logs,file)
        file.close()
        return jsonify({'Message':'Operation Successful'}),200        
    except Exception:
        return jsonify({'Message':'Server Error'}),500
