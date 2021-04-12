def getHeight(root):
    if root is None:
        return 0
    leftHeight=getHeight(root.left)
    rightHeight=getHeight(root.right)
    if leftHeight>rightHeight:
        return leftHeight+1
    else:
        return rightHeight+1
        
