
class Node:
    def __init__(self, key=None, time_stamp=None, due_date=None, value=None, state=None, priority=none):
        self.key = key                  # Cache's key
        self.time_stamp = time_stamp    # Datetime.now() of Master server
        self.due_date = due_date        # Due date defined by Master server
        self.value = value              # Cache's data
        self.state = state              # State of teh data (counter)
