# ========= Here we solve Problems related to linked list ==========

#========== Append last k nodes to start of linked list ==============

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_list:

    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            n = self.head
            while n != None:
                print(f"{n.data}-->" , end =" ")
                n = n.next
            print("NULL",end =" ")

    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        

    def add_end(self,data):
        if self.head == None:
            print("Linked list is empty!")
        else:
            new_node = Node(data)
            n = self.head
            while n.next != None:
                n = n.next
            n.next = new_node
            new_node.next = None

    def add_inbetween(self,data,index):
        if self.head == None:
            print("Linked list is empty!")
        else:
            try:
                new_node = Node(data)
                n = self.head 
                i = 1
                while i != index-1:
                    n = n.next
                    i = i+1
                new_node.next = n.next
                n.next = new_node
            except:
                print("please check you index value")

    def search_in_LL(self,value):
        if self.head == None:
            print("Linked list is empty!")
        else:
            n = self.head
            x = False
            i = 1
            while n != None:
                if n.data == value:
                    x = True
                    break
                else:
                    i = i + 1
                    n = n.next
            if x:
                print(f"Your value {value} is present in linked list at {i} index ")
            else:
                print(f"Your value {value} is not present in linked list")

                
    def delete_start(self):
        if self.head == None:
            print("Linked list is empty!")
        else:
            temp = self.head
            self.head = self.head.next
            del temp
    def delete_end(self):
        if self.head == None:
            print("Linked list is empty!")
        else:
            n = self.head
            while n.next.next != None:
                n =n.next
            temp = n.next
            n.next = None
            del temp

    def delete_in_between(self,value):
        if self.head == None:
            print("Linked list is empty!")
        else:
            n = self.head
            if n.data == value:
                self.delete_start()
            else:
                while n.next.data != value:
                    n = n.next
                temp = n.next
                n.next = n.next.next
                del temp

    def append_k_nodes_at_start(self,k):
        n = self.head
        m = self.head
        count = 1
        count_k = 1
        while n.next is not None :
            n = n.next
            count_k = count_k + 1
        while count != count_k - k:
            m = m.next
            count =count + 1
        n.next = self.head
        self.head = m.next
        m.next = None


         



LL = Linked_list()

LL.add_begin(5)
LL.add_begin(7)
LL.add_end(8)
LL.add_end(9)
LL.add_inbetween(735,4)
# LL.search_in_LL(5)
# LL.delete_start()
# LL.delete_start()
# LL.delete_end()
# LL.delete_in_between(735)
LL.print_LL()
print()
LL.append_k_nodes_at_start(3)
LL.print_LL()
