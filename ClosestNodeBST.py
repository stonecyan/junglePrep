
def findClosestNode(root, k, minDiff, minDiffValue):
    if root is None:
        return
    if root.data==k:
        minDiffValue[0]=root.data
        return
    if minDiff>abs(root.data-k):
        minDiff=abs(root.data-k)
        minDiffValue[0]=root.data
    
    if root.data>k:
        findClosestNode(root.left, k, minDiff, minDiffValue)
    else:
        findClosestNode(root.right,k,minDiff,minDiffValue)
    

root = Node(9) 
root.left = Node(4) 
root.right = Node(17)
root.left.left = Node(3) 
root.left.right = Node(6)
root.left.right.left = Node(5) 
root.left.right.right = Node(7) 
root.right.right = Node(22)
root.right.right.left = Node(20) 
k = 18
minDiff=float('inf')
minDiffValue=[-1]
findClosestNode(root,k, minDiff, minDiffValue)
print(minDiffValue)
