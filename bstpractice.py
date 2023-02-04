


# start by initializing a class node which has a root, and leaves

class Node:
    def __init__(self, value):
        self.value = value 
        self.rightnode = None 
        self.leftnode = None 
    
    
# initialize the binary search tree

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        
    def _insert(self, value, cur_node):
        
        if value < self.cur_node