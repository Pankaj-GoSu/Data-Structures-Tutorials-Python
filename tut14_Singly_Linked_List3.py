#=========== Inserting/ Adding Elements At The End Of The Linked List ===============

'''
# Method name : add_end => data as parameter

For inserting Element at end .
Step1- Create Node
Step2- check liked list is empty or not if empty then we adding our first node.
If Linked List is not Empty : 
step1- Goto Last Node.


'''

#========== Writing Code ==============


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
              
        


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.add_end(100)
LL1.add_end(30)
LL1.print_LL()

