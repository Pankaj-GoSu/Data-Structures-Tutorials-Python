#===== Lowest common Ancestor(LCA) pf two given values in Binary Tree ===============

class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


def preorder(node):
    print(node.data,end = " ")
    if node.lchild:
        preorder(node.lchild)
    if node.rchild:
        preorder(node.rchild)


def findLowestCommonAncestor(root,node1,node2):
    
    if root is None:
        return None
    if (root.data == node1):
        return root
    if (root.data == node2):
        return root
    
    leftlca = findLowestCommonAncestor(root.lchild,node1,node2)
    rightlca = findLowestCommonAncestor(root.rchild,node1,node2)

    if leftlca != None and rightlca != None: # for any node if leftlca and rightlca both are not None than that it is our LCA for those 2 nodes.
        return root # here we return the LCA value.
    
    if leftlca != None: # this is when only one is returning value
        #like if leftlca is None it return rightlca to its caller 
        #like if leftlca is not None it return leftlca to its caller
        return leftlca
    else:
        return rightlca


node =Node(15)
node.lchild = Node(12)
node.rchild = Node(8)
node.lchild.rchild = Node(19)
node.lchild.lchild = Node(13)
node.rchild.lchild = Node(14)
node.rchild.rchild = Node(18)

preorder(node)
print()
print((findLowestCommonAncestor(node,13,18).data))