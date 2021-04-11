def checkBST(root, min, max):
    #base case
    if root is None:
        return True
    
    if root.data<min or root.data>max:
        return False
    
    return checkBST(root.left, min, root.data-1) and checkBST(root.right, root.data+1, max)
