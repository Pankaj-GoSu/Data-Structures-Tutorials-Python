#======== Count all the nodes in a Binary Tree ========


class Binary_Tree:

    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):

        if self.data is None:
            self.data = data
            return
        if self.data > data:
            if self.lchild :
                self.lchild.insert(data)
            else:
                self.lchild = Binary_Tree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_Tree(data)

    def preorder(self):
        
        print(self.data,end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()
    
    def count_nodes_and_sum(self):
        global count
        count = count + 1
        list1.append(self.data)
        if self.lchild:
            self.lchild.count_nodes_and_sum()
        if self.rchild:
            self.rchild.count_nodes_and_sum()
        
        return count
        
def count_recursive(node):
    if node is None:
        return 0
        
    return count_recursive(node.lchild) + count_recursive(node.rchild) + 1

tree1 = Binary_Tree(None)

tree1.insert(5)
tree1.insert(3)
tree1.insert(2)
tree1.insert(7)
tree1.insert(9)
tree1.insert(4)
tree1.insert(6)
tree1.insert(1)
tree1.insert(19)
count = 0
list1 = []
# tree1.preorder()
print(tree1.count_nodes_and_sum())
j = 0
print(list1)
for i in list1:
    j = j + i 
print(j)
# print(count_recursive(tree1))