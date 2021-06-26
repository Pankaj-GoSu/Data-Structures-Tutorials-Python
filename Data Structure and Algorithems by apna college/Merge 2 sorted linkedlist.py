# ======= Merge 2 sorted linked lists ==========


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

    def merge_2_sorted_LL(self,head1,head2):

        ptr1 = head1
        ptr2 = head2
        ptr3 = Node(1) # Dummy Node 
        ptr3.next = self.head
        self.head = ptr3
        n = self.head

        while (ptr1 != None and ptr2 != None):
            
            if ptr1.data > ptr2.data:
                n.next = ptr2
                ptr2 = ptr2.next
                n = n.next
            else:
                n.next = ptr1
                ptr1 = ptr1.next
                n = n.next
        
        while ptr1 != None:
            n.next = ptr1
            ptr1 = ptr1.next
            n = n.next
        
        while ptr2 != None:
            n.next = ptr2
            ptr2 =ptr2.next
            n = n.next
        self.delete_start() # To delete ptr3 Node because it is dummy Node

#========= Recursive method of merging ============                
   
    def merge_recursive(self,new_Node,head1,head2): # it is not completed.
        
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        if head1.data  < head2.data:
            new_Node.next = head1
            self.merge_recursive(new_Node,head1.next,head2)
        else:
            new_Node.next = head2
            self.merge_recursive(new_Node,head1,head2.next)
        
        



LL1 = Linked_list()
LL2 = Linked_list()
LL1.add_begin(9)
LL1.add_begin(7)
LL1.add_begin(5)
LL1.add_begin(4)

LL2 = Linked_list()
LL2.add_begin(6)
LL2.add_begin(3)
LL2.add_begin(1)
LL1.print_LL()
print()
LL2.print_LL()
new_node = Node(1)
# LL1.merge_recursive(new_node,LL1.head,LL2.head)
LL1.merge_2_sorted_LL(LL1.head,LL2.head)
print()
LL1.print_LL()
