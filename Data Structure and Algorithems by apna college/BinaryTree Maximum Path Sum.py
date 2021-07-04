#====== Max path sum =========

'''
Maximum possible sum of a path in the binary tree, starting & ending at any node.
'''
# it is not complete i will do it later.

class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


def Maximum_path_sum(node):
    global max_sum
    if node is None:
        return 0
    max_sum = node.data      
    return max(Maximum_path_sum(node.lchild) + max_sum,Maximum_path_sum(node.rchild)+ max_sum, max_sum) 
    

max_sum = None
node = Node(5)
node.lchild = Node(6)
node.lchild.rchild = Node(7)
node.lchild.rchild.lchild = Node(8)
node.lchild.rchild.rchild = Node(9)


print(Maximum_path_sum(node))