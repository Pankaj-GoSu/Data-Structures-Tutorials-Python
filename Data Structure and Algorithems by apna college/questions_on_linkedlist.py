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
        try:
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
        except:
            print("check k value")

# ============= Find intersection points of 2 linked lists ============
    def intersection_of_LL(self,head1,head2):
        n = head1
        m = head2
        count_1 = 1
        count_2 = 1
        while n.next != None:
            count_1 =count_1 + 1
            n = n.next
        while m.next != None:
            count_2 = count_2 + 1
            m = m.next
       
        if count_1 > count_2:
            n = head1
            m = head2
            count = count_1 - count_2
            i = 0
            while i < count:
                n = n.next
                i = i+1
            j = 0
            while j < count_2:
                if n.data == m.data :
                    print(f"{n.data}")
                    break
                else:
                    n = n.next
                    m = m.next
                    j = j+1
        else:
            n = head1
            m = head2
            count = count_2 - count_1
            i = 0
            while i < count:
                m = m.next
                i = i+1
            j = 0
            while j < count_1:

                if n.data == m.data :
                    print(f"{n.data}")
                    break
                else:
                    j = j + 1
                    n = n.next
                    m = m.next
            
                

        
         



LL1 = Linked_list()
LL2 = Linked_list()
LL = Linked_list()
LL1.add_begin(5)
LL1.add_begin(7)
LL1.add_end(18)
LL1.add_end(9)
LL1.add_inbetween(735,4)

LL2.add_begin(2)
LL2.add_begin(1)
LL2.add_end(3)
LL2.add_begin(11)
LL2.add_end(8)
LL2.add_end(9)
LL2.add_inbetween(735,6)

# LL.search_in_LL(5)
# LL.delete_start()
# LL.delete_start()
# LL.delete_end()
# LL.delete_in_between(735)
LL.intersection_of_LL(LL1.head,LL2.head)
LL1.print_LL()
print()
LL2.print_LL()
# print()
# LL1.append_k_nodes_at_start()
# LL1.print_LL()
