import json

def is_json(data):
    try:
        valid=json.loads(data)
    except  ValueError:
        valid=False
    return valid    