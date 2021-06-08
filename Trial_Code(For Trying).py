
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

