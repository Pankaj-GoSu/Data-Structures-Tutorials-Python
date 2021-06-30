# ======== build Tree from Preorder and Inorder ==========

from typing import OrderedDict



class Tree:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

        

    def tree_constructor(self,preorder,inorder):

        self.data = preorder[0]
        index1 = inorder.index(preorder[0])
        index2 = inorder.index(preorder[0])
        preorder1 = preorder[0:index1+1]
        preorder2 = preorder[index1+1:len(preorder)+1]
        preorder1.pop(0)
        while len(preorder1) != 0:
            index_x = inorder.index(preorder1[0])
            if index_x < index2:
                if self.lchild:
                    self.lchild.data = preorder1[0]
                else: 
                    self.lchild = Tree(preorder1[0])    
            else :
                if self.rchild:
                    self.rchild.data = preorder1[0]
                else:
                    self.rchild = Tree(preorder1[0])
            index1 = index_x
            preorder1.pop(0)
        
        preorder2.pop(0)
        while len(preorder2) != 0:
            index_y = inorder.index(preorder2[0])
            if index_y < index2:
                if self.lchild:
                    self.lchild.data = preorder2[0]
                else: 
                    self.lchild = Tree(preorder2[0])    
            else :
                if self.rchild:
                    self.rchild.data = preorder2[0]
                else:
                    self.rchild = Tree(preorder2[0])
            index2 = index_y
            preorder2.pop(0)
        
        
    def preorder(self):
        print(self.data,end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

preorder =[1,2,4,3,5]
inorder = [4,2,1,5,3]
# index = inorder.index(preorder[0])
# print(index)
tree1 = Tree(None)
tree1.tree_constructor(preorder,inorder)
tree1.preorder()