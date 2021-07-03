# ======= Sum Replacement in Binary Tree ============

'''
Replace the value of each node with the sum of all subtree nodes and itself.

'''

class Binary_Tree:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.data is None:
            self.data = data
            return
        if self.data > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Binary_Tree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_Tree(data)
    
    def preorder(self):

        print(self.data , end= " ")
        if self.lchild :
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

def sum_replacment(node):
    
    if node is None: # it is base condition.
        return

    sum_replacment(node.lchild) # it execute recursively , after it execute we found that we get sum at left node of root node 
    sum_replacment(node.rchild) # it give total sum of right subtree in right node of root node.
    
    if node.lchild and node.rchild: # when both childerens are present
        node.data = node.lchild.data + node.data + node.rchild.data
    
    elif node.lchild: # when only left child is present
        node.data = node.lchild.data + node.data
    
    elif node.rchild: # when only right child is present
        node.data = node.rchild.data + node.data





def preorder(node):

    print(node.data ,end = " ")
    if node.lchild:
        preorder(node.lchild)
    if node.rchild:
        preorder(node.rchild)

tree1 = Binary_Tree(None)

tree1.insert(2)
tree1.insert(1)
tree1.insert(4)
tree1.insert(3)
tree1.insert(5)

preorder(tree1)
sum_replacment(tree1)
print()
preorder(tree1)

