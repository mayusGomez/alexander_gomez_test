import json


class CacheJsonEncoder(json.JSONEncoder):

    def default(self, data):
        try:
            to_serialize = {
                'value': data.value,
                'time_stamp': data.time_stamp,
                'due_date': data.due_date
            }
            return to_serialize
        except AttributeError:
            return super().default(data)
