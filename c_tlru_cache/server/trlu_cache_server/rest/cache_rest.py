import json
from flask import Blueprint, request, Response
from datetime import datetime, timedelta

from ..repository import memory
from ..use_cases.tlru_interact import TLRU_Interaction
from ..serializers.cache_serialize import CacheJsonEncoder
from ..use_cases import response


blueprint = Blueprint('cache', __name__)

STATUS_CODES = {
    response.Response.SUCCESS : 200,
    response.Response.FAIL: 400,
}

@blueprint.route('/cache', methods=['GET', 'POST'])
def cache():

    if request.method == 'POST':
        set_cache = TLRU_Interaction(memory)

        key = ''
        value = None
        minutes = None

        for arg, values in request.args.items():
            if arg == 'key':
                key = values
            if arg == 'value':
                value = values
            if arg == 'minutes':
                minutes = values

        try:
            due_d = None if not minutes else minutes
            due_d = int(due_d)
        except Exception:
            due_d = None

        resp = set_cache.set_node(key=key, time_now=datetime.now(), due_date=due_d, value=value)

        l = set_cache.list_keys()
        print('List of keys:{}'.format(l))
        l = set_cache.list_keys_revert()
        print('List of keys rever:{}'.format(l))

        trl= set_cache.data.get_tlru_cache()
        print('head key:{}  tail key:{}'.format(trl.head.key, trl.tail.key))

        return Response(json.dumps(resp.value, cls=CacheJsonEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[resp.type_response])
    else:
        cache = TLRU_Interaction(memory)
        key = ''
        values = None

        for arg, values in request.args.items():
            if arg == 'key':
                key = values

        if key:
            resp = cache.get_node(key=key)
            return Response(json.dumps(resp.value, cls=CacheJsonEncoder),
                        mimetype='application/json',
                        status=STATUS_CODES[resp.type_response])
        else:
            return Response('Add the key parameter',
                        status=STATUS_CODES[response.Response.FAIL])



    