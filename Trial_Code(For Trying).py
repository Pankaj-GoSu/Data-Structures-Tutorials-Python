
# # Linked List.

# class Node:

#     def __init__(self,data,next):
#         self.data = data
#         self.next = next


# # We create Class Linked List Which Contain 
# # Nodes and Head.

# class LinkedList:

    
#     def __init__(self):
#         self.head = None

#     def Add_Begin(self,data):
#         node = Node(data,self.head)
#         self.head = node
            

#     def Add_End(self,data):
#         n = self.head
#         x = self.head.next
#         while True:
#             if n == None:
#                 node = Node(data,None)
#                 self.head = node
#                 break
#             else:
#                 n = n.next
        
#         self.head = x
     
#     # def In_Between(data,index):
#     #     i = 1
#     #     n = self.head
#     #     while True:

        
        
    
#     def Print_LL(self):
#         global list1
#         if self.head is None:
#             print("Linked List Is Empty")
#         else:
#             n = self.head
#             while n is not None:
#                 print(f" Linked List Contain {n.data}")
#                 list1.append(f"{n.data}-->")
#                 n = n.next

        
# list1 = []
# LL1 = LinkedList()
# LL1.Add_Begin(5)
# LL1.Add_End(10)
# LL1.Add_Begin(15)
# LL1.Add_End(30)
# LL1.Print_LL()
# print(list1)


#================ Inserting In Between ======================


class Node:

    def __init__(self,data): #class constructor or initializtion method.
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None # it means we do not have any node because head is None(Null),It is a Empty Linked List.

    def print_LL(self): # Traversal Operation performed here
        if self.head is None :
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None :
                print(n.data,"-->" , end =" ")
                n = n.ref       

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        else:
            n = self.head
            while n.ref is not None :
                n = n.ref

            n.ref = new_node
              
    def in_Between_add(self,data,index):
        new_node = Node(data)
        i = 1
        n = self.head
        while True:
            if i == index - 1 :
                new_node.ref = n.ref 
                n.ref = new_node
                break
            else:
                i += 1
                n = n.ref
    
    def after_node(self,data,index):
        new_node = Node(data)
        i = 1
        n = self.head
        while True :
            if i == index:
                new_node = n.ref
                n.ref = new_node
                break
            else:
                i += 1
                n = n.ref

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.in_Between_add(50,2)
LL1.add_end(100)
LL1.add_end(30)
LL1.print_LL()



#========== Implementing Binary Search Tree =========


# Here I implementing Binary search tree Using OOP of python.

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
            if n.key == key :
                print("Duplicate values are not allowed") 
            
            while True:
                if n.key > key :
                    if n.left_child is None:
                        n.left_child = new_node
                        break
                    else:
                        n = n.left_child
                elif n.key < key :
                    if n.right_child is None:
                        n.right_child = new_node
                        break
                    else:
                        n = n.right_child

    def print_BST(self): # Here i am writing logic for In-order traversal.
        if self.pointer is None:
            print("Your Binary Search Tree Is Empty")
        else:
            n = self.pointer
           
            for i in range(3):
                if n.left_child == None and n.right_child == None:
                    print(f"<--{n.key}-->" , end = " ")
                    n = None
                elif n.left_child == None:
                    n = n.right_child
                elif n.right_child == None:
                    n = n.left_child
                else :
                     n = n.left_child

               

                

                #     print(f"{n.key}") # here i traverse level wise .
                #     a = self.pointer
                #     b = self.pointer
                #     while True: 
                #         a = n.left_child
                #         if a is not None:
                #             print(f"{a.key}", end = " ")
                #         b = n.right_child
                #         if b is not None:
                #             print(f"{b.key}", end = " ")
                #         if a.left_child is not None:
                #             n = a.left_child
                #             continue
                #         elif b.left_child is not None: 
                #             n = b.right_child
                #             continue
                #         else:
                #             break


                



BST = Binary_search_tree()
BST.insertion(5)
BST.insertion(4)
BST.insertion(8)
# BST.insertion(7)
# BST.insertion(9)
# BST.insertion(12)
BST.print_BST()





