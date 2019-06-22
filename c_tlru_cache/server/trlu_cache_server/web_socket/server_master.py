import asyncio
import json
import logging
import websockets
from datetime import datetime

from trlu_cache_server.use_cases.tlru_interact_master import TLRU_MasterInteraction 
from trlu_cache_server.serializers import cache_serialize
from trlu_cache_server.repository import file_repo

_app_settings = None


async def clients_server(websocket, path):
    logging.info("Server for clients started")
    server_tlru_interact = TLRU_MasterInteraction(file_repo)
    try:
        async for message in websocket:
            logging.debug(f"Message received: {message}")
            message = json.loads(message, cls=cache_serialize.CacheJsonDecoder)
            logging.debug(f"Message json.loads: {message}")

            date_now = datetime.now()

            if message['type'] == 'set_node':
                node = server_tlru_interact.set_node_from_client(message['data'], date_now, SLAVES)
                await websocket.send( json.dumps( {'result': 'true' } ))


            '''if message['type'] == 'set_node':
                value = message['data']['value']
                state = add_state(value)
                confirm_set_node = { 'type': 'confirm_set_node', 'data': { 'value': value, 'state': state } }
                await websocket.send( json.dumps(confirm_set_node) )
                loop = asyncio.get_event_loop()
                loop.create_task(prepare_notify_to_all_last_state())
            else:
                await websocket.send("unsupported event:")
                logging.error("unsupported event:")'''

    finally:
        logging.debug(f"Client unregister")


def execute(settings):
    global _app_settings
    _app_settings = settings

    asyncio.get_event_loop().run_until_complete(
        websockets.serve(clients_server, _app_settings['SERVER']['address'] , 
        _app_settings['SERVER']['port_to_clients'])
    )
    asyncio.get_event_loop().run_forever()
