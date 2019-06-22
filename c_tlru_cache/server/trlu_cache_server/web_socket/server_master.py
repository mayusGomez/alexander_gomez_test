import asyncio
import json
import logging
import websockets

from trlu_cache_server.serializers import cache_serialize


app_settings = None


async def clients_server(websocket, path):
    logging.info("Server for clients started")
    try:
        async for message in websocket:
            logging.debug(f"Message received: {message}")
            message = json.loads(message, cls=cache_serialize.CacheJsonDecoder)
            logging.debug(f"Message json.loads: {message}")

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
    app_settings = settings
    asyncio.get_event_loop().run_until_complete(
        websockets.serve(clients_server, app_settings['SERVER']['address'] , 
        app_settings['SERVER']['port_to_clients'])
    )
    asyncio.get_event_loop().run_forever()
