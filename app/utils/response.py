import uuid
from datetime import datetime
    
def json_result(text, result):
    return {
        '_id': uuid.uuid4().hex,
        'text': text,
        'result': result,
        'createdAt': datetime.now()
    }