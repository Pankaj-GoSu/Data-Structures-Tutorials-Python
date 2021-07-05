#========== Here we make binary Search Tree from preorder ========

class Node:

    def __init__ (self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def buildtree(inorder,preorder,st,end):
    global idx
    if st>end:
        return None
    if idx == len(preorder):
        return None
    
    new_node = Node(preorder[idx])
    index = inorder.index(preorder[idx])
    idx = idx + 1

    if st == end :
        return new_node
    
    new_node.lchild = buildtree(inorder,preorder,st,index-1)
    new_node.rchild = buildtree(inorder,preorder,index+1,end)

    return new_node

def print_Inorder(node):
    if node.lchild:
        print_Inorder(node.lchild)
    print(node.data,end = " ")
    if node.rchild:
        print_Inorder(node.rchild)

def print_preorder(node):
    print(node.data,end = " ")
    if node.lchild:
        print_Inorder(node.lchild)
    
    if node.rchild:
        print_Inorder(node.rchild)


idx = 0

preorder = [10,8,7,2,12,11,17]
inorder = preorder[:]
inorder.sort()
node = buildtree(inorder,preorder,0,len(preorder)-1)
print_Inorder(node)
print_preorder(node)
