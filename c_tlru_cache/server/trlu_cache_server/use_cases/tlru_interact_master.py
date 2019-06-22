import logging
from datetime import datetime, timedelta
import asyncio

from trlu_cache_server.model.node import Node
from trlu_cache_server.data_structures import cache_nodes
from .constants import DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE, NODES_LIMIT_CUANTITY


class TLRU_MasterInteraction:

    def __init__(self, data):
        self.data = data
        logging.debug(f"Load use case, setters len: { len(data.get_tlru_cache().setters) }")


    async def broadcast_to_slaves(self, slaves, rm_node):
        """
        parameters:
            slaves: dict with key = slaves(websocket) to send new state
            rm_node: node removed
        """
        def notify_to_all(slaves, slave, slave_state, last_state, rm_node):
            """
            Process the broadcast to slave and update slave state (syncronized)
            parameters:
                slaves: dict wirth slaves
                slave: slave to send
                slave_state: slave state syncronized with master
                last_state: last state node
            """
            data_to_slave = {
                'new_node' : {
                    'key': last_state.key,
                    'value': last_state.value,
                    'due_date': last_state.due_date,
                    'due_date_stamp': last_state.due_date_stamp,
                    'state'last_state.state,
                },
                'removed_node': { 
                    'key': rm_node.key if rm_node else None,
                    'value': rm_node.value if rm_node else None,
                    'due_date': rm_node.due_date if rm_node else None,
                    'due_date_stamp': rm_node.due_date_stamp if rm_node else None,
                    'state'rm_node.state if rm_node else None,
                }
            }
            await slave.send(json.dumps(get_last_state()))
            # Verify if the slave is syncronized
            if value == last_state - 1:
                slaves[slave] = last_state.state
                set_slave_state(slave, last_state)

        if slaves:       # asyncio.wait doesn't accept an empty list
            cache = self.data.get_tlru_cache()
            # Get last state from deque
            last_state = cache.data_state[-1]

            # Prepare list to broadcast at same time
            slaves_to_send = []
            for slv, slave_state in slaves.items():
                slaves_to_send.append(notify_to_all(slaves, slv, slave_state, last_state, rm_node))
            
            if len(slaves_to_send ) > 0:
                await asyncio.wait(slaves_to_send)

    async def set_node_from_client(self, node_message, date_now, slaves=None):
        """
        Receive:
            node_message : Data from cliente
            date_now : datetime.now
            slaves: dict with the slaves to boradcast info and state

        Verify if the node is in setters
            If it is: 
                remove node from priority_structure
                add new node to priority_structure
            else
                add new node to priority_structure
        Add node to setters
        add node to status
        Return the node
        async broadcast to slaves
        """
        logging.debug(f"Arrive node data: { data }")
        cache = self.data.get_tlru_cache()

        # If the 'minutes' data is None, then assign a big due_date, else add the timedelta to now
        due_date = None
        if node_message['minutes'] == None:
            logging.debug(f"Minutes is None, assign big due date")
            due_date = date_now + timedelta(days=DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE)
        else:
            logging.debug(f"Minutes not is None, assign timedelta")
            due_date = date_now + timedelta(minutes=node_message['minutes'])

        node = Node(
            key = node_message['key'],
            date_stamp = date_now,
            due_date = due_date.isoformat(),
            due_date_stamp = datetime.timestamp(due_date) ,
            value = node_message['value'],
            state = self.data.get_next_state()
        )

        rm_node = None

        if node_message['key'] in cache.setters:
            # Remove node from priority structure
            cache_nodes.remove_node(cache.priority_structure, cache.setters[node_message['key']])          
            # replace in setters
            cache.setters[node_message['key']] = node
            # Add node to priority_structure
            cache_nodes.push_node(node)
            cache.data_state.append(node)
        else:
            # Verify len of structure for remove a node
            if len(cache.setters) >= NODES_LIMIT_CUANTITY:
                rm_node = cache_nodes.pop_node(cache.priority_structure)
                del cache.setters[rm_node.key]

                # Add new node
                cache.setters[node.key] = node
                cache_nodes.push_node(cache.priority_structure, node)
                cache.data_state.append(node)

        # Save to disk
        self.data.save_tlru_cache()

        # Broadcats to slaves:
        loop = asyncio.get_event_loop()
        loop.create_task(self.broadcast_to_slaves(slaves, rm_node))
        return node
               





