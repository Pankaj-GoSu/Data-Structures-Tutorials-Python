#====== Left view of a Binary Tree ========

'''
it means what nodes are visible to us when we see from left side.
--> It is done by level by level so here we do level wise traversal
--> In each level we print left most node only of each level.

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
    
    def level_order_traversal(self):

        queue = [self] # it contain top most node or current node (not value).
        next_queue = [] # it conatains childs of current nodes.
        level = [] # in level list we put or value of nodes level wise.
        result = [] # this store final list of lists of every level

        while queue != []: # it run till queue not become empty.

            for nodes in queue:
                level.append(nodes.data)
                if nodes.lchild:
                    next_queue.append(nodes.lchild)
                if nodes.rchild:
                    next_queue.append(nodes.rchild)
            queue = next_queue # here we update our queue
            next_queue = [] # reinitialize
            result.append(level) # here we store list of value in each level
            level = [] # reinitialize
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

list_lvl = tree1.level_order_traversal()
print("Left view of tree is:")
left_view = []
for lists in list_lvl:
    left_view.append(lists[0])

print(left_view)