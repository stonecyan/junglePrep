class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
 
 
class BSTtoDll:
    def __init__(self):
        self.head = None
        self.prev = None
 
    def convert(self, root):
       
        # Base case
        if root is None:
            return
           
        # Recursively convert left subtree
        self.convert(root.left)
         
        # Now convert this node
        node = root
        if self.head is None:
            self.head = node
        else:
            self.prev.right = node
            node.left = self.prev
        self.prev = node
         
        # Finally convert right subtree
        self.convert(root.right)
        return self.head
 
 
def BinaryTreetoDLL(root):
    converter = BSTtoDll()
    return converter.convert(root)
 
 
def print_dll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.right
 
 

root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)
 
# convert to DLL
head = BinaryTreetoDLL(root)
 
# Print the converted list
print_dll(head)
