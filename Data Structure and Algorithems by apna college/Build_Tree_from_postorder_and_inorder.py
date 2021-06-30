#======= Build Tree from postorder and inorder ==========


from typing import NewType


class Node:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


def buildtree(postorder,inorder,st,end):
    global idx
    if st > end:
        return
    
    if idx == -1:
        return

    new_node = Node(postorder[idx])
    index = inorder.index(postorder[idx])
    idx = idx - 1

    if st == end:
        return new_node
    
    new_node.rchild = buildtree(postorder,inorder,index+1,end)
    new_node.lchild = buildtree(postorder,inorder,st,index-1)
    
    return new_node

def inorder_print(node):
    if node is None:
        return
    
    inorder_print(node.lchild)
    print(node.data,end = " ")
    inorder_print(node.rchild)

postorder = [4,2,5,3,1] 
inorder = [4,2,1,5,3]
idx = len(postorder) - 1

root = buildtree(postorder,inorder,0,4)
inorder_print(root)