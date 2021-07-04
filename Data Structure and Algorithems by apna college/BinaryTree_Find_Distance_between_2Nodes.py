#========== Find distance between 2 nodes of a binary tree =============

'''
The distance between two nodes is minimum number of edges to be traversed to reach one node from another.

'''

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



def FindLowestCommonAncestor(root,node1,node2):
    if root is None:
        return
    
    if (root.data == node1):
        return root
    
    if (root.data == node2):
        return root
    
    leftlca = FindLowestCommonAncestor(root.lchild,node1,node2)
    rightlca = FindLowestCommonAncestor(root.rchild,node1,node2)

    if leftlca != None and rightlca != None:
        return root

    if leftlca != None:
        return leftlca
    else:
        return rightlca

def distance_between_two_nodes(root,node1,node2):
    """
    This is for find distance between 2 nodes 
    --> here first we find Lowest common ancestor node.
    --> then we realise we get common ancestor so we now use a function which give 
        distance between LCA node to given values of node then we add both values and get our result.
    """
    if root is None:
        return 
    
    lca = FindLowestCommonAncestor(root,node1,node2)
    d1 = []
    d2 = []
    distanceFromParenttoNode(lca,node1,d1,0)
    distanceFromParenttoNode(lca,node2,d2,0)
    
    return d1[0] + d2[0]


def distanceFromParenttoNode(root,value,height,level): # This is important function it give .
    # it will give distance between one node to a perticular node whose value is given.


    if root is None :
        return
    
    if root.data == value:
        height.append(level)
    
    distanceFromParenttoNode(root.lchild,value,height,level+1)
    distanceFromParenttoNode(root.rchild,value,height,level+1)

    



node =Node(15)
node.lchild = Node(12)
node.rchild = Node(8)
node.lchild.rchild = Node(14)
node.lchild.lchild = Node(13)
node.rchild.lchild = Node(14)
node.rchild.rchild = Node(18)

d = distance_between_two_nodes(node,13,14)
# preorder(node)
print(d)