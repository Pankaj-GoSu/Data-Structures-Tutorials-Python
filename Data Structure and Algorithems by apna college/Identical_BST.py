# ========= Identical Binary Search Tree =============


'''
Here identical means they store same value in them or not it is not about structully same.
--> To find two BST are identical or not we just find any trversal operation then
    compare both trversal result if both are same then we can se they are identical BST. 

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


def inorder(node,list1):
    if node.lchild:
        inorder(node.lchild,list1)
    list1.append(node.data)
    if node.rchild:
        inorder(node.rchild,list1)

# This code is for identical and identical by structure.

def same_tree(node1,node2):
    
    if node1 is None and node2 is None:
        return True
    
    if node1 is not None and node2 is not None:
        return ((node1.data == node2.data) and 
                        same_tree(node1.lchild,node2.lchild) and
                        same_tree(node1.rchild,node2.rchild))
    
    return False

    



bst1 = Binary_Search_Tree(None)
bst2 = Binary_Search_Tree(None)

bst1.insert(10)
bst1.insert(8)
bst1.insert(6)
bst1.insert(7)
bst1.insert(14)
bst1.insert(16)
bst1.insert(12)
bst1.insert(18)

bst2.insert(10)
bst2.insert(8)
bst2.insert(6)
bst2.insert(7)
bst2.insert(14)
bst2.insert(16)
bst2.insert(12)
bst2.insert(18)
list1 = []
list2 = []
inorder(bst1,list1)
inorder(bst2,list2)

print(list1)
print(list2)
if list1 == list2:
    print("Both the tree contains same value")
else:
    print("Both the tree contains different value")

print(same_tree(bst1,bst2))