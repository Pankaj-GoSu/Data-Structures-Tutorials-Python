# ======== Binary Search Tree (BST)=========

'''
Binary search tree is like binary tree with some conditions:
'''

class Binary_Search_Tree:

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
                self.lchild = Binary_Search_Tree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_Search_Tree(data)

    def preorder(self):
        print(self.data,end =" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()


bts = Binary_Search_Tree(None)

bts.insert(10)
bts.insert(14)
bts.insert(17)
bts.insert(7)

bts.preorder() 