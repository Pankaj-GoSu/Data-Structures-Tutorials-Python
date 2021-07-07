#=========== Check for Binary Search Tree =============

'''
To check weather valid BST or not  we do:

#we know in order of BST is in increasing order. 

'''

class Node:

    def __init__ (self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

# class Binary_Search_Tree:

#     def __init__(self,data):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
    
#     def insert(self,data):
#         if self.data is None:
#             self.data = data
#             return
#         if self.data > data:
#             if self.lchild:
#                 self.lchild.insert(data)
#             else:
#                 self.lchild = Binary_Search_Tree(data)
#         else:
#             if self.rchild:
#                 self.rchild.insert(data)
#             else:
#                 self.rchild = Binary_Search_Tree(data)


    
def valid_BST(node):
    if node.lchild:
        valid_BST(node.lchild)
    bst_list.append(node.data)
    if node.rchild:
        valid_BST(node.rchild)

# bts = Binary_Search_Tree(None)

# bts.insert(10)
# bts.insert(14)
# bts.insert(5)
# bts.insert(17)
# bts.insert(7)
# bts.searching(11)
bst_list = [] 
# node = Node(10)
# node.lchild = Node(1)
# node.rchild = Node(13)
# node.lchild.lchild = Node(5)
node = Node(10)
node.lchild = Node(3)
node.rchild = Node(13)
node.lchild.lchild = Node(4)
valid_BST(node)
print(bst_list)
x = bst_list[0]
for i in bst_list:
    if x <= i:
        x = i
    else:
        print("it is not valid bst")
        break

if x == bst_list[-1]:
    print("it is valid bst")
