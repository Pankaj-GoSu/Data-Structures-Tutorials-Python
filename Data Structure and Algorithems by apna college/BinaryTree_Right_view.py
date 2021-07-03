# ============== Right view of a binary tree ==============

'''
It means what nodes are visible to us when we see from right side.
--> It is done by level by level so here we do level wise traversal
--> In each level we print right post node only.

'''

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
            if self.lchild:
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

    def level_order_Traversal(self):

        queue = [self] # it store top most node (not value)
        next_queue = [] # it store next elements of our tree or childs of current node
        level = [] # it store level wise value.
        result = [] # it store final value in list of list format.

        while queue != []:

            for nodes in queue:
                level.append(nodes.data)
                if nodes.lchild:
                    next_queue.append(nodes.lchild)
                if nodes.rchild:
                    next_queue.append(nodes.rchild)
            queue = next_queue
            next_queue = []
            result.append(level)
            level = []
        return result
tree1 = Binary_Tree(None)

tree1.insert(10)
tree1.insert(7)
tree1.insert(8)
tree1.insert(9)
tree1.insert(5)
tree1.insert(15)
tree1.insert(16)
tree1.insert(17)
tree1.insert(14)
tree1.insert(13)
tree1.insert(12)
tree1.insert(11)

list_lvl =tree1.level_order_Traversal()

print(list_lvl)
print("right view of tree is :")
right_view = []
for lists in list_lvl:
    right_view.append(lists[-1])
print(right_view)
