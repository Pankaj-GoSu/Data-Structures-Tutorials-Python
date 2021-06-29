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
        elif self.lchild == None:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Binary_tree(data)
            
        elif self.rchild == None:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_tree(data)

tree1 = Binary_tree(None)

tree1.insert(10)