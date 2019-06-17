from ..rest.response import Response
from ..model.node import Node

class TLRU_Interaction:

    def __init__(self, data):
        self.data = data

    def get_node(self, key):
        try:
            node = self.data[key]
            
        except KeyError:
            return Response(Node())


    def set_node(self, node):
        #exists = node.setters
        pass