import json


class CacheJsonDecoder(json.JSONDecoder):
    def default(self, data):
        try:
            to_serialize = {
                'type': data.value,
                'data': data.data
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
