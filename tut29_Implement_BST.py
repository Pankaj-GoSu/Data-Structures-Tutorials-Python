# ==== Python Program To implement Binary Searach Tree ============

"""
Every Node of binary search tree contains:
key / data
left child
right child

"""

class Binary_Search_Tree:

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Binary_Search_Tree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_Search_Tree(data)




root = Binary_Search_Tree(None)
root = Binary_Search_Tree(10)