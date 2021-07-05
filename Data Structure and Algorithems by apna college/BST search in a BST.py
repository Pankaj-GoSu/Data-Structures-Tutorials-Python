# ===== Search and Delete in Binary search Tree =======

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

    def searching(self,val):
        if self.data == val:
            print("value is present in BST")
            return
        if self.data > val:
            if self.lchild:
                self.lchild.searching(val)
            else:
                print("Value is not present in BST")
        else:
            if self.rchild:
                self.rchild.searching(val)
            else:
                print("Value is not present in BST")

#======== Delete in binary search tree ==========
    
    def deletion(self,val,current):

        if self.data is None:
            print("Tree is Empty")
            return
        if self.data > val:
            if self.lchild:
                self.lchild = self.lchild.deletion(val,current)
            else:
                print("Given key does not exit !")
        elif self.data < val :
            if self.rchild:
                self.rchild = self.rchild.deletion(val,current)
            else:
                print("Given key does not exit !")

        else:
            if self.lchild is None:
                temp = self.rchild
                if val == current: # here we copy right node to root node then we delete right node.
                    self.data = self.rchild.data
                    self.lchild = self.rchild.lchild
                    self.rchild = self.rchild.rchild
                    temp = None
                    return
                self = None
                return temp
            
            if self.rchild is None:
                temp = self.lchild
                if val == current: # here we copy left node to root node and then we delete left node.
                    self.data = self.lchild.data
                    self.lchild = self.lchild.lchild
                    self.rchild = self.lchild.rchild
                    temp = None
                self = None
                return temp
            
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.data = node.data

            self.rchild = self.rchild.deletion(node.data,current)
        return self # it is bcoz we return our root node of BST.


    def preorder(self):
        print(self.data,end =" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)


bts = Binary_Search_Tree(None)

bts.insert(10)
bts.insert(14)
bts.insert(5)
# bts.insert(17)
# bts.insert(7)
# bts.searching(11)
bts.preorder() 
print()
if count(bts)>1:
    bts.deletion(10,bts.data)
else:
    print("can't perform deletion operation !")


bts.preorder()
print()
print(count(bts))