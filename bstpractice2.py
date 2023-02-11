"""
 Copyright 2023 Eddy Ndumia

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

      https://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
 """




class Node:
    
    # tip: after creating a class we initiate the class using a constructor, be sure to know 
    # what you are doing at all times
    def __init__(self, value):
        # the class has 3 members, a value and leftnode and rightnode
        self.value = value
        self.right_node = None
        self.left_node  = None
        
        
    # next we need to insert data into our tree
    
    #but before we do, we need another class called Binary_Search_Tree that will help us in inserting values into the tree
    
class Binary_Search_Tree:
    
    # init
    
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value_ins, cur_node):
        if value_ins < cur_node.value:
            if cur_node.left_node is None:
                cur_node.left_node = Node(value_ins)
            else:
                self._insert(value_ins, cur_node.left_node)
                
        elif value_ins > cur_node.right_node:
            if cur_node.right_node is None:
                cur_node.right_node = Node(value_ins)
            else:
                self._insert(value_ins, cur_node.right_node)
                
        else:
            print('value already inserted xD')
        
        
    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)
            
            
        def _print_tree(self, cur_node):
            if cur_node is not None:
                _print_tree(cur_node.left_node)
                print(str(cur_node.value))
                _print_tree(cur_node.right_node)
        
        

def fill_tree (self, maxelem=100, maxint=1000):
    from random import randint
        
    for _ in range(maxelem):
        input_elems = randint(0, maxint)
        tree.insert(input_elems)
    return tree
    
tree = Binary_Search_Tree()

tree = fill_tree(tree)

tree.print_tree