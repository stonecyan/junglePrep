#https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
#https://www.geeksforgeeks.org/find-distance-between-two-nodes-of-a-binary-tree/

class Node:
    def __init__(self, data):
        self.data = data 
        self.left = self.right = None
# Function to insert nodes in level order 
def insertLevelOrder(arr, root, i, n):
    # Base case for recursion 
    if i < n:
        temp = Node(arr[i]) 
        root = temp 

        # insert left child 
        root.left = insertLevelOrder(arr, root.left,
                                     2 * i + 1, n) 

        # insert right child 
        root.right = insertLevelOrder(arr, root.right,
                                      2 * i + 2, n)
    return root

def arrayToBST():
    arr = [1, 2, 3, 4, 5, 6, 6, 6, 6]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n) 


def pathBetweenNodes(root, path, d):
      # base case handling
    if root is None:
        return False
 
     # append the node value in path
    path.append(root.data)
  
    # See if the k is same as root's data
    if root.data == d :
        return True
  
    # Check if k is found in left or right
    # sub-tree
    if ((root.left != None and pathToNode(root.left, path, d)) or
            (root.right!= None and pathToNode(root.right, path, d))):
        return True
  
    # If not present in subtree rooted with root,
    # remove root from path and return False
    path.pop()
    return False
 
  
def distanceBetweenNodes():
   if root:
        # store path corresponding to node: data1
        path1 = []
        pathToNode(root, path1, data1)
 
        # store path corresponding to node: data2
        path2 = []
        pathToNode(root, path2, data2)
 
        # iterate through the paths to find the
        # common path length
        i=0
        while i<len(path1) and i<len(path2):
            # get out as soon as the path differs
            # or any path's length get exhausted
            if path1[i] != path2[i]:
                break
            i = i+1
 
        # get the path length by deducting the
        # intersecting path length (or till LCA)
        return (len(path1)+len(path2)-2*i)
    else:
        return 0
 
