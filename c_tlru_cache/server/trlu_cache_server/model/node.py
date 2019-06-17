
class Node:
    def __init__(self, time_stamp, due_date, value, next_node, previous_node):
        self.time_stamp = time_stamp
        self.due_date = due_date
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node
