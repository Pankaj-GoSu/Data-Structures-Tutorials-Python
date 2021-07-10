# =========== Zig zag Traversal of Binary Search Tree ============

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

    def level_order(self):
        if self is None:
            return
        queue = [self] 
        next_queue = []
        level = [] # store value in list of current node
        result = []

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

bst = Binary_Search_Tree(None)  

bst.insert(10)
bst.insert(8)
bst.insert(6)
bst.insert(7)
bst.insert(14)
bst.insert(16)
bst.insert(12)
bst.insert(18)
result = bst.level_order()
print(result)
print("Zig zag Traversal of bst")
for i in range(len(result)):
    if i%2 == 0:# when i is even then it print left to right
        for j in range(len(result[i])):
            print(result[i][j],end = " ")
    else: # it print right to left when i is odd.
        for j in range(len(result[i])-1,-1,-1):
            print(result[i][j],end = " ")
                    