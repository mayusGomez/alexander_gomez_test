import json


class CacheJsonEncoder(json.JSONEncoder):

    def default(self, data):
        try:
            to_serialize = {
                'value': data.value 
            }
            return to_serialize
        except AttributeError:
            return super().default(data)
