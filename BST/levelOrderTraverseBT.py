def levelOrderTraverse(root):
    if root is None:
        return
    
    q=[]
    
    q.append(root)
    while len(q)>0:
        print(q[0].data)
        node=q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
