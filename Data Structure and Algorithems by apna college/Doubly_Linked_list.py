# ============ Doubly Linked List ==============

class Node:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class Doubly_LinkedList:

    def __init__(self):
        self.head = None

    def print_DLL_forward(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            n = self.head
            print("NULL",end="")
            while n != None:
                print(f"<--{n.data}-->",end = "")
                n = n.next
            print("NULL")
    def print_DLL_backword(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            n = self.head
            while n.next != None:
                n= n.next
            print("NULL",end="")
            while n!=None:
                print(f"<--{n.data}-->",end = "")
                n = n.prev
            print("NULL")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None: 
            new_node.next = self.head
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
    
    def add_end(self,data):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            new_node =Node(data)
            n = self.head
            if n.next is None:
                new_node.prev = n
                n.next = new_node
                new_node.next = None
            else:
                while n.next.next is not None:
                    n =n.next
                new_node.prev = n.next
                n.next.next = new_node
                new_node.next = None
    def add_in_between(self,data,index):
        if self.head == None:
            print("Doubly Linked list is Empty")
        else:
            new_node = Node(data)
            n = self.head
            if index == 1:
                self.add_begin(data)
            else:
                count = 1
                while count != index-1:
                    n = n.next
                    count += 1

                new_node.prev = n.next.prev
                new_node.next = n.next
                n.next.prev = new_node
                n.next = new_node

    def delete_begin(self):
        if self.head == None:
            print("Doubly Linked list is Empty")
        else:
            self.head = self.head.next
            self.head.prev = None        

    def delete_by_value(self,value):
        if self.head == None:
            print("Doubly Linked list is Empty")
        else:
            n = self.head
            if n.data == value:
                self.delete_begin()
            else:
                while n.next.data != value:
                    n = n.next
                if n.next.next == None:
                    n.next.prev = None
                    n.next = None
                else:    
                    n.next.next.prev = n.next.prev
                    n.next = n.next.next


Dll = Doubly_LinkedList()
Dll.add_begin(5)
Dll.add_begin(6)
Dll.add_begin(8)
Dll.add_end(7)
Dll.add_end(11)
Dll.add_end(9)
Dll.add_in_between(735,3)
Dll.add_in_between(73,1)
Dll.delete_begin()
# Dll.delete_by_value(8)
Dll.delete_by_value(9)
Dll.delete_by_value(11)

print("Forword is:")
Dll.print_DLL_forward()
print("Backword is:")
Dll.print_DLL_backword()