# ========== Print all nodes at distance k ========

# It is not complete i will do it later. 
class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


def nodes_at_distance_k(root,nodes_list,k):

    if root is None:
        return
    
    if k == 0:
        nodes_list.append(root.data)

    nodes_at_distance_k(root.lchild,nodes_list,k-1)
    nodes_at_distance_k(root.rchild,nodes_list,k-1)




node = Node(5)
node.lchild = Node(6)
node.lchild.rchild = Node(7)
node.lchild.rchild.lchild = Node(8)
node.lchild.rchild.rchild = Node(9)

nodes_list =[]
nodes_at_distance_k(node,nodes_list,3)
print(nodes_list)