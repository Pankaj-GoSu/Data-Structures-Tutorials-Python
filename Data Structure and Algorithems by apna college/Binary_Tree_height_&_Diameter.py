#========== Height and Diameter in binary Tree =======

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

        print(self.data , end= " ")
        if self.lchild :
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def height_and_Diameter(self): # Here i do Level wise traversal and 
        # store the value in list and len of that list is height of tree
        if self is None:
            return
        queue = [self] # firstly it store root node (not value complete node)
        next_queue = [] # it store child of root node or child of child means it store next queue
        level = [] # it store level wise value of nodes
        result = [] # it contain list of list and give us level wise Traversal result

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

def height(node): # here we also said that height is total no. of nodes from
                  # leaf node to root node taking longest path

    if node is None:
        return 0
    return 1 + max(height(node.lchild),height(node.rchild))


def diameter(node): # Diameter is : Number of nodes in the longest path between any 2 leaves
    
    if node is None:
        return 0 # base case when tree is empty.

    
    lheight = height(node.lchild)
    rheight = height(node.rchild)

    ldiameter = diameter(node.lchild)
    rdiamete = diameter(node.rchild)

    return max(lheight + rheight + 1 , ldiameter , rdiamete)


tree1 = Binary_Tree(None)

# tree1.insert(6)
# tree1.insert(5)
# tree1.insert(7)
# tree1.insert(8)

tree1.insert(10)
tree1.insert(7)
tree1.insert(15)
tree1.insert(14)
tree1.insert(13)
tree1.insert(12)
tree1.insert(16)
tree1.insert(17)
tree1.insert(18)
tree1.insert(19)

# tree1.preorder()
a = tree1.height_and_Diameter() # it return a list of list.
#Height of tree is equal to total no. of level 
print(f"height of tree is {len(a) - 1}")

# Height of Binary Tree:
print(height(tree1)) 
print(diameter(tree1))