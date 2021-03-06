# ====== Reversing a Linked List ==========

'''

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

    def reverse_LL_iterative(self): # it reverse our linked list 
        # here we make 3 pointer,previous ,current and next.

        previous = None
        current = self.head
        
        while current != None:
            next = current.next
            current.next = previous
            previous = current
            current = next
            
        self.head = previous
    
    def reverse_LL_Recursive(self,n): # not working now i will make it work after some time

        if n == None or n.next == None:
            return 
        else:
            new_head = self.reverse_LL_Recursive(n.next)
            n.next.next = n
            n.next = None

            self.head =new_head

# ========= Reverse k nodes in a linked list ===============

    def reverse_K_nodes(self,head,k): # not completed
        current = head
        next = None
        prev = None
        count = 0
 
        # Reverse first k nodes of the linked list
        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
 
        # next is now a pointer to (k+1)th node
        # recursively call for the list starting
        # from current. And make rest of the list as
        # next of first node
        if next is not None:
            head.next = self.reverse_K_nodes(current, k)
 
        # prev is new head of the input list
        return prev
        


LL = Linked_list()

LL.add_begin(5)
LL.add_begin(7)
LL.add_end(8)
LL.add_end(9)
LL.add_end(6)
LL.add_inbetween(735,4)
# LL.search_in_LL(5)
# LL.delete_start()
# LL.delete_start()
# LL.delete_end()
# LL.delete_in_between(735)
LL.print_LL()
print()
# LL.reverse_LL_iterative()

# LL.reverse_LL_Recursive(LL.head)
LL.head = LL.reverse_K_nodes(LL.head,2) # here we change head to starting previous value.
LL.print_LL()