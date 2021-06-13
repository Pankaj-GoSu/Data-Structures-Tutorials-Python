# ==== Python Program To implement Binary Searach Tree ============

"""
Every Node of binary search tree contains:
key / data
left child
right child

"""

class Binary_Search_Tree:
   

    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = Binary_Search_Tree(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = Binary_Search_Tree(data)

    def search(self,data):
        if self.key == data:
            print("Node is Found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print(" Node is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print(" Node is not found")

    def delete(self,data,current):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,current)
            else:
                print("Given node is not present in this tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,current)
            else:
                print("Given node is not present in this tree")

        else: # data == self.key

            if self.lchild is None:
                temp = self.rchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                else:
                    self = None
                    return temp # this method returns temp value to its caller .
            
            elif self.rchild is None:
                temp = self.lchild
                if data == current:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                else:
                    self = None
                    return temp

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key # here we replace node with smallest value in right side 
            self.rchild = self.rchild.delete(node.key,current)
        
        return self # it return to where it is call from here .


    def max_key(self):
        node = self
        while node.rchild:
            node = node.rchild
        
        print(f"max value is{node.key}")

    def min_key(self):
        node = self
        while node.lchild:
            node = node.lchild

        print(f"min value is {node.key}")
   
    def pre_order(self): # root , left , right.
        print(self.key, end = " ")
        if self.lchild:
            self.lchild.pre_order()# it pause the execution and it execute self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order() # it pause the execution and it execute self.rchild.pre_order()


    def in_order(self): # left , root , right.
        if self.lchild:
            self.lchild.in_order()
        print(self.key, end = " ")
        if self.rchild:
            self.rchild.in_order()

    def post_order(self):
        if self.lchild:
            self.lchild.post_order()
        if self.rchild:
            self.rchild.post_order()
        print(self.key, end = " ")

# for count how many nodes in BST
def count(node):
    if node is None:
        return 0
    return 1 + count(node.lchild) + count(node.rchild)

root = Binary_Search_Tree(None)
# for i in range(100):
#     root.insert(i)
root.insert(8)
root.insert(12)
root.insert(5)
root.insert(7)
root.insert(9)
root.insert(132)
root.insert(4)
root.insert(3)
root.insert(2)
# root.insert()

if count(root) > 1:
    root.delete(2,root.key)
else:
    print("can't perform deletion operation")
print()
root.pre_order()
print()
root.in_order()
print()
root.post_order()
print()
root.max_key()
root.min_key()

