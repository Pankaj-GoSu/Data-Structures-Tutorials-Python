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

    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(" Node is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(" Node is not found")


    def pre_order(self): # root , left , right.
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.pre_order()# it pause the execution and it execute self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order() # it pause the execution and it execute self.rchild.pre_order()


    def in_order(self): # left , root , right.
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end = " ")



root = Binary_Search_Tree(None)
# for i in range(100):
#     root.insert(i)
root.insert(2)
root.insert(12)
root.insert(4)
root.insert(7)
root.insert(9)
root.insert(1)
print()
root.pre_order()
print()
root.in_order()
print()
root.post_order()