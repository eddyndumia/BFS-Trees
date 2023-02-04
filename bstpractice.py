


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
        
        if value < self.cur_node:
            if self.leftnode is None:
                self.leftnode = Node(value)
            else:
                self._insert(value, self.leftnode)
        elif value > self.cur_node:
            #check if right node has a value
            if self.rightnode is None:
                #if it does not have a value, start another instance of the class with the rightnode as the root
                self.rightnode = Node(value)
            else:
                #else recursively insert using the private function _insert
                self._insert(value, self.rightnode)
                
                #if value already in tree
        else:
            print("Value already in tree")
            
            
    def print_tree(self):
        self.root != None:
            self.__print_tree(self.root)
            
    def __print_tree(self, cur_node):
        if self.cur_node is not None:
            __print_tree(cur_node.leftnode)
            print(str(self.cur_node))
            __print_tree(cur_node.right)
            
    def fill_tree(self, maxint=100, maxelem=1000):
        from random import randint 
        for _ in range(maxint):
            elems = radint(0, maxelem)
            tree.insert(maxelem)
        return tree
        
        
tree = Binary_Search_Tree()

tree = fill_tree(tree)

tree.print_tree
        
    
        
        
        