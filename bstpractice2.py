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
            