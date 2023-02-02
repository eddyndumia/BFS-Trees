

# binary trees simple

class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data

    def insert(self, data):
        if self.data is None:
            self.data = data
        else:
            if data < self.data:
                if self.left is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    # inserting recursively
                    self.right.insert(data)

root = Node("z")
root.insert('a')
root.insert('b')
root.insert('c')
root.insert('d')
root.insert('q')
root.insert('e')

