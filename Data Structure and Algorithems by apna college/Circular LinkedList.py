# ========= Circular Linked list ===========

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Circular_LL:

    def __init__(self):
        self.head = None

    def print_CLL(self):

        if self.head is None:
            print("Circular Linked List")
        else:
            n = self.head
            
            while n.next != self.head:
                print(f"{n.data}-->",end = "")
                n = n.next
            print(f"{n.data}-->",end = "")
    
    def add_begin(self,data):

        if self.head is None:
            new_node = Node(data)
            new_node.next = new_node
            self.head = new_node

        else:
            new_node = Node(data)
            new_node.next = self.head
            n = self.head
            while n.next != self.head:
                n = n.next
            n.next = new_node
            self.head = new_node

    def add_end(self,data):
        if self.head is None :
            print("Circular Linked List Empty")
        else:
            new_node = Node(data)
            n = self.head
            while n.next is not self.head:
                n = n.next
            n.next = new_node
            new_node.next = self.head

    def add_in_between(self,data,index):
        if self.head is None:
            print("Circular Linked List Empty")
        else:
            new_node = Node(data)
            n = self.head
            count = 1
            while count != index -1:
                n = n.next 
                count += 1
            new_node.next = n.next
            n.next = new_node
            
    def del_start(self):
        n = self.head
        while n.next is not self.head:
            n = n.next
        n.next = self.head.next
        self.head = self.head.next


    def del_end(self):
        n = self.head
        while n.next.next is not self.head:
            n = n.next
        n.next = self.head

    def del_by_value(self,value):
        n = self.head
        if n.data == value:
            self.del_start()
        else:
            while n.next.data != value:
                n = n.next
                n.next = n.next.next

CLL = Circular_LL()

CLL.add_begin(5)
CLL.add_begin(7)
CLL.add_begin(3)
CLL.add_begin(6)
CLL.add_end(7)
CLL.add_in_between(735,3)
# CLL.del_start()
# CLL.del_end()
CLL.del_by_value(6)

CLL.print_CLL()