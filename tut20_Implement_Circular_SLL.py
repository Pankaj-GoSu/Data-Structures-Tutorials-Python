# Here I am Implementing Circular Singly Linked List:

class Node: # first we make node class for creating node

    def __init__(self,data):
        self.data = data
        self.next = None


class Circular_SLL:

    def __init__(self):
        self.head = None
        
    def add_begin(self,data):
        if self.head is None:
            print("Circular Linked List is empty")
        else:
            new_node = Node(data)
            new_node.next = self.head
            n = self.head
            while n.next != self.head :
                n = n.next
            n.next = new_node
            self.head = new_node
    
    def add_end(self,data):
        if self.head is None:
            print("Circular Linked List is empty")
        else:
            new_node = Node(data)
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head

    def add_In_between(self,data,index):
        """ This function insert node between linked list according to given index value"""
        new_node = Node(data)
        i = 1
        n = self.head
        while i != index-1 :
            n = n.next
            i += 1
        new_node.next = n.next
        n.next =new_node
    
    def add_first(self,data):
        new_node = Node(data)
        new_node.next = new_node
        self.head = new_node
        
    def del_begin(self):
        if self.head is None :
            print("Empty Linked List")
        else:
            n = self.head 
            while n.next is not self.head:
                n = n.next
            self.head = self.head.next
            n.next = self.head

    def del_end(self):
        if self.head is None:
            print("Empty Linked List")
        else:
            n = self.head
            while n.next.next is not self.head:
                n = n.next
            n.next = self.head
        
    def del_by_value(self,value):
        if self.head is None:
            print("Empty Linked List")
        else:
            n = self.head
            i = 1
            while n.data is not value: # with this i am calculating index of given value element .
                n = n.next
                i += 1
            m = self.head
            j = 1
            while True:
                if i == 1:
                    self.del_begin()
                    break
                elif j == i-1:
                    m.next = n.next
                    break
                else:
                    j += 1
                    m = m.next

    def print_CSLL(self): # This function is for traversal the Circular Linkedlist
        if self.head is None:
            print("CSLL is Empty")
        else:
            n = self.head
            while n.next is not self.head:
                print(f"{n.data}-->", end = " ")
                n = n.next
            print(f"{n.data}-->", end = " ")

CSLL = Circular_SLL()
CSLL.add_first(3)
CSLL.add_begin(5)
CSLL.add_begin(7)
CSLL.add_end(10)
CSLL.add_end(4)
CSLL.add_In_between(735,5)
CSLL.del_begin()
CSLL.del_end()
CSLL.del_by_value(735)
CSLL.print_CSLL()