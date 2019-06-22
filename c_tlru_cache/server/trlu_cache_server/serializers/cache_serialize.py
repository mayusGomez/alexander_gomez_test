import json


class CacheJsonDecoder(json.JSONDecoder):
    def default(self, data):
        try:
            to_serialize = {
                'type': data.type,
                'data': {
                    'key': data.data.key,
                    'value': data.data.value,
                    'minutes': data.data.minutes
                }
            }
            return to_serialize
        except AttributeError:
            return super().default(data)


class CacheJsonEncoder(json.JSONEncoder):
    def default(self, data):
        try:
            to_serialize = {
                'type': data.value 
            }
            return to_serialize
        except AttributeError:
            return super().default(data)
