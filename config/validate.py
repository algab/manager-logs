from functools import wraps
from flask import request, abort, jsonify
from jsonschema import validate, ValidationError

def validate_request(schema):
    def decorator(f):
        @wraps(f)
        def validate_schema(*args,**kwargs):
            data = request.get_json()
            try:
                validate(data,schema)
            except ValidationError as e:
                return jsonify({'Message':e.message}), 400
            return f(*args, **kwargs)
        return validate_schema
    return decorator    
