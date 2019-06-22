from datetime import timedelta

from .response import Response
from ..model.node import Node
from .constants import DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE, NODES_LIMIT_CUANTITY


class TLRU_MasterInteraction:

    def __init__(self, data):
        self.data = data



'''
class TLRU_Interaction:

    def __init__(self, data):
        self.data = data

    def _move_to_rigth(self, node=None):
        """
        Move the node to rigth (worst position)
        """
        tlru_data = self.data.get_tlru_cache()
        
        while node.next_node and node.due_date < node.next_node.due_date:
            tmp_node_b = Node(
                next_node=node.next_node.next_node 
            )
            tmp_b = node.next_node

            # Evaluate if node is head
            if tlru_data.head == node:
                tlru_data.head = node.next_node
            # Evaluate if node.next_node is tail
            if node.next_node == tlru_data.tail:
                tlru_data.tail = node

            tmp_b.previous_node = node.previous_node
            tmp_b.next_node =  node

            if node.previous_node:
                node.previous_node.next_node = tmp_b

            node.next_node = tmp_node_b.next_node
            node.previous_node = tmp_b

    def _move_node_to_left(self, node=None):
        """
        When a "get" operation found a node, this node is moved to a better position
        """ 
        tlru_data = self.data.get_tlru_cache()
        while node.previous_node and node.due_date >= node.previous_node.due_date:         
            # Evaluate if node is tail
            if tlru_data.tail == node:
                tlru_data.tail = node.previous_node
            # Evaluate if node.previous is head
            if node.previous_node == tlru_data.head:
                tlru_data.head = node
            
            node_pp = node.previous_node.previous_node if node.previous_node else None
            node_p = node.previous_node
            node_n = node.next_node 

            if node_pp:
                node_pp.next_node = node
            node_p.next_node = node_n
            node_p.previous_node = node
            node.next_node = node_p
            node.previous_node = node_pp
            node_n.previous_node = node_p

    def get_node(self, key):
        """
        Return the node if exists in cache, and re-order to a better position
        Return FAIL if not exists
        """
        try:
            tlru_data = self.data.get_tlru_cache()
            # If the key exists, then return the node and move the node to a better position 
            node = tlru_data.setters[key]

            # Re-order node to a better position
            self._move_node_to_left(node)

            return Response(Response.SUCCESS, node)

        except KeyError:
            node = Node()
            return Response(Response.FAIL, node)

    def set_node(self, key=None, time_now=None, due_date=None, value=None):
        """
        Set a node to the cache, if the node exists, reorder the cache
        if the node doesn't exists then insert node and delete last nodein the cache if lenght is full
        """
        
        try:
            tlru_data = self.data.get_tlru_cache()
            # If the key exists, then return the node and re-order node with the due_date
            node = tlru_data.setters[key]
            node.time_stamp = time_now, 
            node.due_date = due_date if due_date else time_now + timedelta(days=DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE)
            node.value = value
            
            if node.previous_node and node.due_date >= node.previous_node.due_date:
                self._move_node_to_left(node)
            elif node.next_node and node.due_date < node.next_node.due_date:
                self._move_to_rigth(node)  

            return Response(Response.SUCCESS, node)

        except KeyError:
            node = Node(
                key=key,
                time_stamp= time_now, 
                due_date= due_date if due_date else time_now + timedelta(days=DAYS_TO_ADD_NODE_WITHOUT_DUE_DATE), 
                value=value, 
                next_node=None, 
                previous_node=None
            )
            self._insert_new_node(node)
            return Response(Response.SUCCESS, node)

    def _evaluate_del_node(self):
        """
        Determine if the nodes cuantity is superior than max, and fix 
        """
        tlru_data = self.data.get_tlru_cache()
        
        if tlru_data.count > NODES_LIMIT_CUANTITY:
            # del tlru_data.setters[tlru_data.tail.key
            tlru_data.tail = tlru_data.tail.previous_node
            tlru_data.tail.next_node = None
            del tlru_data.setters[tlru_data.tail.key]
            tlru_data.count -= 1

    def _insert_new_node(self, node=None):
        """
        Insert a new node in the cache
        """
        print('insert node')
        tlru_data = self.data.get_tlru_cache()
        tlru_data.setters[node.key] = node
        if not tlru_data.head:
            print('insert first node')
            tlru_data.head = node
            tlru_data.tail = node
            tlru_data.count = 1
            
        else:
            # insert node at head
            print('insert node in head')
            node.next_node = tlru_data.head
            tlru_data.head.previous = node
            tlru_data.head = node
            node.next_node.previous_node = node

            tlru_data.count += 1

            # If the due date is less than the vext node, then move the node to rigth
            if  node.due_date < node.next_node.due_date:
                print('move to rigth')
                self._move_to_rigth(node)

            self._evaluate_del_node()

    def list_keys(self, max_iter=10):
        """
        Return a list with the keys of cache
        """
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

    def list_keys_revert(self, max_iter=10):
        """
        Return a list with the keys of cache
        """
        tlru_data = self.data.get_tlru_cache()
        node = tlru_data.tail
        keys = [node.key]
        iterations=1
        while node.previous_node and iterations < max_iter:
            iterations+=1
            tmp_node = node.previous_node
            keys.append(tmp_node.key)

            node = node.previous_node

        return keys
'''