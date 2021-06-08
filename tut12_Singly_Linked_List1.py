# ========== Implement Singly Linked List ==================

# Linked list is chain of Nodes.

# How To Implement Singly Linked List

'''

For Traversal Linked list: We Make one class (Print_LL)

1- Linked List Is Empty:
    if "head is None" it means Linked List is empty.
    So Print a Msg that Linked List is Empty.

2-  If it is not Empty:
    # We begin process from head.
    n = self.head 
    n.data or self.head.data --> Give data
    n.ref or self.head.ref --> Give ref

---> print(n.data) # it print data of present Node.
    n = n.ref # it give address of next Node.
'''

#Step 1- Creating a Node.

class Node:

    def __init__(self,data): #class constructor or initializtion method.
        self.data = data
        self.ref = None


node1 = Node(10)

#Step 2- We make Another class to link these indivisual Nodes. (LinkedList class).

# LinkedList Contains Node and head .
class LinkedList:

    def __init__(self):
        self.head = None # it means we do not have any node because head is None(Null),It is a Empty Linked List.

    def print_LL(self):
        if self.head is None :
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None :
                print(n.data)
                n = n.ref       

LL1 = LinkedList()
LL1.print_LL()






