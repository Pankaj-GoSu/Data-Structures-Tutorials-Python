#========== Trying To make complete binary tree with all operations ==========

# =========== I will do it later ================

class Node: # we make this class to create node of tree

    def __init__(self,key): # this function is a constructor of class Node.(key-->data)

        self.key = key
        self.left_child = None
        self.right_child = None

class Binary_search_tree:

    def __init__(self): # this function is a constructor of class Binary_search_tree.

        self.pointer = None
    
    def insertion(self,key):
        
        if self.pointer is None:

            print("Tree is empty \n wait we are making Tree for you... \n \t \t Your Root Node is ready!")
            new_node = Node(key)
            self.pointer = new_node

        else:
            n = self.pointer # self.pointer is object of class Node so with this we can access any node .
            new_node = Node(key) 
            
            while True:
                if n.key == key : # if inserting value is duplicate then we didn't allow
                    print("Duplicate values are not allowed")
                    break
                elif n.key > key : # if inserting value less then node value then we see its left child is present or not if not present then we add new key to that place
                    if n.left_child is None:
                        n.left_child = new_node
                        break
                    else: # if left child is present then we move to left child
                        n = n.left_child
                elif n.key < key :
                    if n.right_child is None:
                        n.right_child = new_node
                        break
                    else:
                        n = n.right_child

    def search_in_BST(self,key): # This function is for search any value in tree
        n = self.pointer
        while True:
            if n.key == key : # if root node value  is same as key
                print(f"Your {key} value is present in tree")
                break
            elif key < n.key : # if root node value greater then key value
                if n.left_child == None: # if given value which is less then node value then we go to left side and suppose left subtree does not exit it means key value not present
                    print(f"Your {key} value is not present in tree")
                    break
                else:
                    n = n.left_child # we go to left node
                    if n.key == key: #if key is same as root node(root node here is left child) value
                        print(f"Your {key} value is present in tree")
                        break
                    elif n.left_child == None and n.right_child == None: # if node has no child then key value is not present
                        print(f"Your {key} value is not present in tree")
                        break
                    elif n.left_child == None: # if left child is not present then we go to right child
                        n = n.right_child
                    elif n.right_child == None:# if right child is not present then we go to right child
                        n = n.left_child
                
            elif n.key < key : # if root node value less then key value
                # See above comment for your refernce
                if n.right_child == None:
                    print(f"Your {key} value is not present in tree")
                    break
                else:
                    n = n.right_child
                    if n.key == key:
                        print(f"Your {key} value is present in tree")
                        break
                    elif n.left_child == None and n.right_child == None:
                        print(f"Your {key} value is not present in tree")
                        break
                    elif n.left_child == None:
                        n = n.right_child
                    elif n.right_child == None:
                        n = n.left_child


            # This is also for searching values
    def search(self,key): # here i use recursive method 
        n = self.pointer 
        while True: #while loop is used for recursive operation
            if n.key == key:
                print(f"Your {key} value is present in tree")
                break
            elif key < n.key:
                if n.left_child:
                    n = n.left_child # from here it again start from while loop
                else:
                    print("Value Not found")
                    break
            elif key > n.key:
                if n.right_child:
                    n = n.right_child # from here it again start from while loop
                else:
                    print("Value Not found")
                    break
            else:
                print("Value not found")
                
    
    # def pre_order_print(self): # first root then left subtree then right subtree.
    #     n = self.pointer 
    #     while n.left_child is not None:
    #         print(f"{n.key}")
    #         n = n.left_child
        
    #     while n.right_child is not None:

        
            


               

                


                



BST = Binary_search_tree()
# for i in range(100):
#     BST.insertion(i)
BST.insertion(15)
BST.insertion(3)
BST.insertion(2)
BST.insertion(5)
BST.insertion(4)
BST.insertion(1)
BST.insertion(7)
# BST.insertion(13)
# BST.insertion(20)
# BST.insertion(50)
# BST.insertion(0)
# BST.insertion(1)
# BST.insertion(72)
# BST.insertion(17)
# BST.search_in_BST(25)
# BST.search_in_BST(12)
# BST.search_in_BST(0)
# BST.search_in_BST(72)
# BST.search_in_BST(10000)
# BST.search(15)
# BST.search(150)
# BST.search(18)
# BST.search(15)
# BST.search(150000)
# BST.search(99)
BST.pre_order_print()

# BST.print_BST()

