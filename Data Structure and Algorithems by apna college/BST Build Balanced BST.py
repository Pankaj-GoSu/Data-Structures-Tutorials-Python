#============ Build Balanced BST from sorted Array ==============



class Node:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None


# class Balanced_BST:

#     def __init__(self,data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None

#     def insert(self,data):
#         if self.data is None:
#             self.data = data
#         if self.data > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = Balanced_BST(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = Balanced_BST(data)
    
def preorder(node):
        
    print(node.data,end = " ")
    if node.lchild:
        preorder(node.lchild)
    if node.rchild:
        preorder(node.rchild)
    
def inorder(node):
    if node.lchild:
        preorder(node.lchild)
    print(node.data,end = " ")
    if node.rchild:
        preorder(node.rchild)





a = [1,2,3,4,5]

# bst = Balanced_BST(None)

def inserting(a,st,end): # it generate balanced binary search tree
    
    if st > end:
        return 
    mid = int((st+end)/2)
    node = Node(a[mid])
    node.lchild = inserting(a,st,mid-1)
    node.rchild = inserting(a,mid+1,end)
    return node
node = inserting(a,0,len(a)-1)
print(node)
preorder(node)
print()
inorder(node)


