class Tree(object):
    def __init__(self, hash_, children):
        self.hash_ = hash_
        self.children = children if children else []