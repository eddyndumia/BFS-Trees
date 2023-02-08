


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
        
        # check the value of the root of the object from class Node which is #value
        if value < cur_node.value:
            #if value of #current root node/leaf is greater than the value we have, we assign it to the left node of this current node
            if cur_node.leftnode is None:
                cur_node.leftnode = Node(value)
            else:
                self._insert(value, cur_node.leftnode)
        elif value > cur_node.value:
            #if value of #current root node/leaf is greater than the value we have, we assign it to the left node of this current node
            #check if right node has a value
            if cur_node.rightnode is None:
                #if it does not have a value, start another instance of the class with the rightnode as the root
                    cur_node.rightnode = Node(value)
            else:
                #else recursively insert using the private function _insert
                self._insert(value, cur_node.rightnode)
                
                #if value already in tree
        else:
            print("Value already in tree")
            
            
    def print_tree(self):
        if self.root is not None:
            self.__print_tree(self.root)
            
        def __print_tree(self, cur_node):
            if self.cur_node is not None:
             __print_tree(cur_node.leftnode)
             print(str(self.cur_node))
             __print_tree(cur_node.right)
            
def fill_tree(tree, maxint=100, maxelem=1000):
    from random import randint 
    for _ in range(maxint):
        elems = randint(0,maxelem)
        tree.insert(elems)
    return tree
        
        
tree = Binary_Search_Tree()

tree = fill_tree(tree)

tree.print_tree
        
    
        
        
        