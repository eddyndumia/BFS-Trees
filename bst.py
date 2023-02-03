# Binary Search Tree // Fenwick Tree --> DSA

class Node:
    def __init__(self,value=None):
        ## initiate the nodes, and root
        self.value = value #root
        self.right = None #right node
        self.left = None #left node
        
class Binary_Search_Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left is None:
                cur_node.left = Node(value)
            else:
                self._insert(value,cur_node.left)
        elif value > cur_node.value:
            if cur_node.right is None:
                cur_node.right = Node(value)
            else:
                self._insert(value, cur_node.right)
        else:
            print("Value already in Node!")
                


    def print_tree(self):
     if self.root != None:
        self._print_tree(self.root)
    
    
    def _print_tree(self, cur_node):
        if cur_node is not None:
            self._print_tree(cur_node.right)
            print(str(cur_node.value))
            self._print_tree(cur_node.left)
            
            
def fill_tree(self, t = 100, w = 1000):
        from random import randint
        for _ in range(t):
            elem = randint(0,w)
            tree.insert(elem)
        return tree
    
# tree is the instance of the class Binary Search Tree
# while Binary Search Tree is the structure / class/ blueprint
tree = Binary_Search_Tree()

tree = fill_tree(tree)
tree.print_tree()


        
            
        
