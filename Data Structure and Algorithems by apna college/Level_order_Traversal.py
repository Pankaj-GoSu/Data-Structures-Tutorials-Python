#======= Level Order Traversal ,Sum at Kth Level in Binary Tree ========

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
    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.data,end = " ")
        if self.rchild:
            self.rchild.inorder()

    def level_order(self): # important
        if self is None:
            return
        queue = [self] # it store root node (not value) 
        next_queue = [] # it will store next level values means child or root node.
        level = [] # it store value of root , mainly it store value first root then we reinitialize it then it store child values
        result = [] # it store list of list in which we get result of level_order Traversal.

        while queue != []:
            for root in queue:
                level.append(root.data)
                if root.lchild:
                    next_queue.append(root.lchild)
                if root.rchild:
                    next_queue.append(root.rchild)
            queue = next_queue
            next_queue = []
            result.append(level)
            level = []
        return result

# ======== Sum of kth level ===========
    def sum_kth_level(self,k):
        list1 = self.level_order()
        list2 = list1[k]
        sum_kth = 0
        for val in list2:
            sum_kth = sum_kth + val
        
        print(f"Sum of kth level is: {sum_kth}")




tree1 = Binary_Tree(None)

tree1.insert(5)
tree1.insert(3)
tree1.insert(2)
tree1.insert(7)
tree1.insert(9)
tree1.insert(4)
tree1.insert(6)
tree1.insert(1)
arr = []
# tree1.preorder()
print(tree1.level_order())
tree1.sum_kth_level(1)
# tree1.inorder()