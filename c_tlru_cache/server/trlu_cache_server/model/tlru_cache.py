
class TLRU_Cache:

    def __init__(self):
        self.count = 0
        self.setters = {}
        self.head = None
        self.tail = None
