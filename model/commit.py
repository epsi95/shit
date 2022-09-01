class Commit(object):
    def __init__(self, hash_, prev, child, message):
        self.hash_ = hash_
        self.prev = prev
        self.child = child
        self.message = message
