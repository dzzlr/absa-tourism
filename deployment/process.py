import uuid
from datetime import datetime
from model import ABSATourism
    
def json_result(text, result):
    return {
        '_id': uuid.uuid4().hex,
        'text': text,
        'result': result,
        'createdAt': datetime.now()
    }

def send_to_endpoint(object: dict):
    result = ABSATourism(object['text'])
    object_result = json_result(object['text'], result.result)
    object['data'] = object_result
        
    del object['text']
    return object