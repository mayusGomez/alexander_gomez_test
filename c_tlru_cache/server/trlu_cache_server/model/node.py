
class Node:
    def __init__(self, key=None, time_stamp=None, due_date=None, value=None, next_node=None, previous_node=None):
        self.key = key
        self.time_stamp = time_stamp
        self.due_date = due_date
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node
