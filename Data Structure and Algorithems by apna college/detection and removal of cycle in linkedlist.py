# ============= Detection and Removal of cycle in linked list ============

'''
Floyed's Algorithem
OR
Hare and Tottoise Algorithm

'''

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
            count = 1
            while n != None:
                print(f"{n.data}-->" , end =" ")
                n = n.next
                count = count + 1
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

    def make_cycle(self,data,index):
        if self.head is None:
            print("empty ll")
        else:
            new_node = Node(data)
            n = self.head
            m = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            count = 1
            while count != index-1:
                m = m.next
                count = count +1
            new_node.next = m.next

    def detect_cycle(self):
        slow = self.head
        fast = self.head

        while(fast!=None and fast.next !=None):
            slow = slow.next
            fast = fast.next.next

            if (fast == slow):
                return True
        
        return False

    def deletion_cycle(self):
        slow = self.head
        fast = self.head

        while(fast!=None and fast.next!=None):
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                break
        fast = self.head
        while(fast.next != slow.next):
            fast = fast.next
            slow = slow.next
        slow.next = None


#=============== Remove Cycle From Linked List ====================
'''
Here we make fast or slow means we make one pointer to point head and then we move
both pointer by 1-1 step and when both pointers next point to same then which pointer in cycle we
make it to point to next
'''


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
# LL.make_cycle(11,3)
LL.make_cycle(12,2)
print(LL.detect_cycle())
# LL.deletion_cycle()
LL.deletion_cycle()
LL.print_LL() 