# ======= Balanced Height in a binary tree =========


'''
For each node,the difference between the heights of the left subtree & right subtree <= 1(absolute value).
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

        print(self.data,end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
# ====== Balanced height Binary Tree =======

def height(node):
    if node is None:
        return 0
    return max(height(node.lchild), height(node.rchild)) + 1

def Balanced_tree_height(node):  # it tells that tree is balanced binary tree or not
    global flag
    if node is None:
        return 
    lheight = height(node.lchild)
    rheight = height(node.rchild)
    Balanced_tree_height(node.lchild) # it call rescursivly 
    Balanced_tree_height(node.rchild)
    
    if lheight - rheight <= 1 and rheight - lheight <=1: # it means absolute diffrence is equal or less then 1.
        flag = True    
    else:
        flag = False
        return flag
    
    return flag
         

flag = False
tree1 = Binary_Tree(None)

tree1.insert(10)
tree1.insert(8)
tree1.insert(7)
tree1.insert(11)
tree1.insert(12)
tree1.insert(13)
tree1.insert(14)
# tree1.insert(6)
# tree1.insert(5)


print(height(tree1))
Balanced_tree_height(tree1)

if flag:
    print("Balanced")
else:
    print("Not Balanced")
