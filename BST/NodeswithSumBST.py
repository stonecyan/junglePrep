class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

#Store in sorted array
#traverse tree in order and add to list
def inorder(root, list):
    if root is None:
        return
    inorder(root.left, list)
    list.append(root.data)
    inorder(root.right, list)

def findNodes(root, _sum):
    if root is None:
        return False
    node_list=[]
    inorder(root, node_list)
    i=0
    j=len(node_list)-1
    output=[]
    while i<j:
        if node_list[i]+node_list[j]==_sum:
            output.append([node_list[i],node_list[j]])
            break
        if node_list[i]+node_list[j]<_sum:
            i+=1
        else:
            j-=1
        print(output)
    return output

#store in dictinoary
def helper(root, dict, _sum):
    if root is None:
        return False
    if _sum-root.data in dict:
        print(f'{root.data}, {_sum-root.data}')
        return True
    dict[root.data]=1
    return helper(root.left, dict, _sum) or helper(root.right, dict, _sum)
    

def findNodesDict(root, _sum):
    nodeDict={}
    return helper(root, nodeDict, _sum)

root=Node(15)
root.left=Node(10)
root.right=Node(20)
root.left.left=Node(8)
root.left.right=Node(12)
root.right.left=Node(16)
root.right.right=Node(25)
k=33
findNodesDict(root, k)
