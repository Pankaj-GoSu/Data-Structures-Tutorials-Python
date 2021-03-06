# =========== Inserting item At Begining ====================

'''
# For Inserting element in begining
Step1- Create node. Means we make an object from Node class.
Step2- new_node.ref = head
Step3- head = new_node # we store object new_node in head.
#Pint To Remeber is Object Cantain memory address where it store so when we give
"head =new_node" head contain address of new node.
# when we make a object from class Node it has already an address which is refernce of new created Node.

'''
#=========== Writing Program for it =============

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
                print(n.data)
                n = n.ref       

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node



LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)

LL1.print_LL()



