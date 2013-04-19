class Node:
    name = ""
    before = set()
    after = set()
    prev = None
    next = None
    def __init__(self, name):
        self.name = name
        self.before = set()
        self.after = set()
        self.prev = None
        self.next = None



