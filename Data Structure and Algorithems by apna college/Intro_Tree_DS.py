#============ Binary Tree Introduction ===============


'''
Binary Tree : every node has maximum only 2 childerens.

'''

#Properties of Binary Trees:

'''
1--> Maximum nodes at level L = 2^L.
2--> Maximum nodes in a tree of height H is 2^H-1 or total no. of level L .
3--> For N nodes , minimum possible height or minimum number of levels are log2(N+1)
4--> A binary tree with L leaves has at least log2(N+1)+1 number of levels 
'''

class Binary_tree:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.data == None:
            self.data = data
            return
        if self.data >  data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Binary_tree(data)
        else:    
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_tree(data)

    def preorder(self):
        print(self.data,end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data,end = " ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.data,end =" ")

tree1 = Binary_tree(None)

tree1.insert(10)
tree1.insert(12)
tree1.insert(13)

tree1.insert(11)
tree1.insert(14)
tree1.insert(15)

tree1.preorder()
print()
tree1.inorder()
print()
tree1.postorder()