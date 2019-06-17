from datetime import timedelta

from .response import Response
from ..model.node import Node
from .constants import YEARS_TO_ADD_NODE_WITHOUT_DUE_DATE, NODES_LIMIT_CUANTITY


class TLRU_Interaction:

    def __init__(self, data):
        self.data = data

    def get_node(self, key):
        try:
            tlru_data = self.data.get_tlru_cache()
            # If the key exists, then return the node and move the node to a better position 
            node = tlru_data.setters[key]
            while node.previous_node and node.due_date >= node.previous_node.due_date:
                tmp_node = Node(
                    next_node=node.next_node
                )
                # Evaluate if node is tail
                if tlru_data.tail == node:
                    tlru_data.tail = node.previous_node
                # Evaluate if node.previous is head
                if node.previous_node == tlru_data.head:
                    tlru_data.head = node

                # Assing data to re-order cache
                if node.previous_node.previous_node:
                    node.previous_node.previous_node.next_node = node
                
                node.next_node = node.previous_node
                node.previous_node = node.previous_node.previous_node

                node.next_node.previous_node = node
                node.next_node.next_node = tmp_node.next_node

            return Response(Response.SUCCESS, node)

        except KeyError:
            return Response(Response.FAIL, Node())

    def set_node(self, key=None, time_now=None, due_date=None, value=None):
        node = Node(
            key=key,
            time_stamp= time_now, 
            due_date= due_date if due_date else time_now + timedelta(days=DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE), 
            value=value, 
            next_node=None, 
            previous_node=None
        )
        
        try:
            tlru_data = self.data.get_tlru_cache()
            # If the key exists, then return the node and re-order node with the due_date
            node_exists = tlru_data.setters[key]
            
            if node.due_date != node_exists.due_date:
                node_exists.previous.next_node = node_exists.next_node
                node_exists.next_node.previous_node = None
                # TODO: Delete node and insert in another position

            return Response(Response.SUCCESS, node)

        except KeyError:
            _insert_new_node(tlru_data, node)
            return Response(Response.SUCCESS, node)

    def remove_node(tlru_data=None):


    def _evaluate_del_node(tlru_data=None):
        if tlru_data.count > NODES_LIMIT_CUANTITY:
            tlru_data.tail.previous_node.next_node = None
            tlru_data.tail = tlru_data.tail.previous_node
            tlru_data -= 1

    def _insert_new_node(tlru_data=None, node=None):
        if not tlru_data.head:
            tlru_data.head = node
            tlru_data.tail = node
            tlru_data.count = 1
            tlru_data.setters = {
                node.key: node
            }
        else:
            # Verify the new node have more time than head 
            if tlru_data.head.due_date < node.due_date:
                tlru_data.head.previous_node = node
                node.next_node = tlru_data.head
                tlru_data.head = node
                tlru_data.count += 1

            tmp_node = tlru_data.head
            while tmp_node.next_node:
                if node.due_date >= tmp_node.due_date:
                    tmp_node.next = node
                    node.previous_node = tmp_node
                    node.next_node = tmp_node.next_node
                    tmp_node.previous_node = node

            # Veryfy insert node, if not then is the last
            if node.previous_node == None and node.next_node == None:
                tlru_data.tail.next_node = node
                node.previous_node = tlru_data.tail
                tlru_data.tail = node

            _evaluate_del_node(tlru_data)


    def list_keys(self, max_iter=10):
        tlru_data = self.data.get_tlru_cache()
        node = tlru_data.head
        keys = [node.key]
        iterations=1
        while node.next_node and iterations < max_iter:
            iterations+=1
            tmp_node = node.next_node
            keys.append(tmp_node.key)

            node = node.next_node

        return keys

