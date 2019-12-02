import json
from datetime import datetime
from config.redis import cache

def save_logs(doc):   
    data = cache.get('logs')
    if data == None:
        data = []
        doc['date'] = str(datetime.now())
        data.append(doc)
        cache.set('logs', json.dumps(data))
    else:
        data = json.loads(data)
        doc['date'] = str(datetime.now())
        data.append(doc)
        cache.set('logs', json.dumps(data))