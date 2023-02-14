'''
Linked Lists

    They are a form of sequential collection that does not need to be in order.
    They are not contagious
    They occur in nodes, where each node has the address to the next node's memory address
    They are flexible in insertion and deletion
    To reference an object in this data structure, you have to traverse through the entire struct from head - 
    till you the object you are looking for, unlike in arrays and lists where indexes are used or dictionaries where keys are used
 

There are four types of Linked Lists:
 
 Singly Linked Lists:
 They execute in a linear way where each node has the adress to the next node only and the tail has a null pointer
 Like a train probably
 
 Circular Singly Linked Lists
 They are the same as singly linked lists but the last node(not tail) has an address to the first node (not head)
 For example, when playing a game of chess, each player makes a play and then the game starts from the beginning again.
 This structure goes in a circular way
 
 Double Linked Lists
 In doubly linked lists each node contains an address to the first node and an address to the last node as well
 Like in a music playlist where you can go back and forth through songs.
 
 Circular Double Linked Lists
 In circular doubly linked lists, each nde contains an address to the next node's memory (address location) as well as the prevoius as in double 
 linked lists. However, the 1st node contains an address to the last node and the 2nd node, while the last node has the address to the previous node 
 and the first one as well.
 
'''