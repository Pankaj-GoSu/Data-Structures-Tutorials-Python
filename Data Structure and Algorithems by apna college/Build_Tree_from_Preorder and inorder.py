# ======== build Tree from Preorder and Inorder ==========

class Node:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def buildtree(preorder,inorder,st,end):
    global idx
    if idx == len(preorder):
        return None
    
    if (st>end):
        return None
    
    new_node = Node(preorder[idx])
    
    index1 = inorder.index(preorder[idx])
    
    idx = idx +  1
    
    if st == end:
        return new_node

    new_node.lchild = buildtree(preorder,inorder,st,index1-1)
    new_node.rchild = buildtree(preorder,inorder,index1+1,end)

    return new_node

def prInorder(node):
 
    if (node == None):
        return
         
    prInorder(node.lchild)
    print(node.data, end = " ")
    prInorder(node.rchild)

def postorder(node):
    if node == None:
        return
    postorder(node.lchild)
    postorder(node.rchild)
    print(node.data,end =" ")
idx = 0
preorder = [1,2,4,3,5]
inorder = [4,2,1,5,3]

root = buildtree(preorder,inorder,0,4)
prInorder(root)
print()
postorder(root)