class Node:
    def __init__(self, value):
        self.data=value
        self.left=None
        self.right=None

def printPath(path, i):
    output=[]
    for j in range(i, len(path)):
        output.append(path[j])
    print(output)

def findPaths(root, path, k):
    if root is None:
        return
    path.append(root.data)
    
    findPaths(root.left, path, k)
    findPaths(root.right, path, k)
    
    sum=0
    for j in range(len(path)-1, -1, -1):
        sum+=path[j]
        if sum==k:
            printPath(path, j)
    
    path.pop(-1)

root = Node(1) 
root.left = Node(3) 
root.left.left = Node(2) 
root.left.right = Node(1) 
root.left.right.left = Node(1) 
root.right = Node(-1) 
root.right.left = Node(4) 
root.right.left.left = Node(1) 
root.right.left.right = Node(2) 
root.right.right = Node(5) 
root.right.right.right = Node(2) 
k = 5
path=[]
findPaths(root, path, k)
