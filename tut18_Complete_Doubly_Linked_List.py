
# Here I am Writing Complete Operations of Doubly Linked List With Explnation:

class Node: #Making a Node class to creat a node.
    
    def __init__(self,data): # Constructor for Node class take data as argument.
        self.data = data
        self.prev = None
        self.next = None


class Doubly_Linked_List():

    def __init__(self): # Constructor for Linkedlist class
        self.head = None

    def print_DLL(self):
        if self.head is None:
            print("Doubly Linked List is Empty")
        else:
            n = self.head # giving address of head to n so that we can traverse linked list without changing head postion.
           
            while n is not None:
                print(f"<--{n.data}-->",end = " ")
                n = n.next
    
    # self.head is become object for Node class bcoz we assign Node class object to this.
    # and with the help of self.head we can access Complete Node (means Data , Prev address , Next address).
    def add_begin(self,data):
        ''' This function add any node at begin'''
        new_node = Node(data)
        if self.head is None:
            print("This Is Your First Node so you can not add Node at begining \n But I will making first Node of Your")
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_end(self,data):# this function add node at end taking self.head as a object of Node class.
        new_node = Node(data)
        n = self.head
        if self.head is None:
            print("This Is Your First Node so you can not add Node at begining \n But I will making first Node of Your")
            self.head = new_node
        else:
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.prev = n

    def add_before(self,data,value): 
        '''This function add node before given given value'''
        new_node = Node(data)
        if self.head is None:
            print("Your Linked List is empty")

        else:
            n = self.head
            i =1
            while n.data != value: #here we find index of Node which contain that given value. 
                n = n.next
                i += 1
            
            n = self.head
            j = 1
            while True: # we have index of that node whose value is given show we stop before that node and add new node
                if j == i-1:
                    new_node.next = n.next
                    n.next = new_node
                    new_node.prev = n
                    n = n.next # here we go to next node means our desire node and assign new node value to its prev link.
                    n.prev = new_node
                    break
                else:
                    n = n.next
                    j += 1
        
    def add_after(self,data,value):
        new_node = Node(data)
        if self.head is None:
            print("Linked List is Empty")
        else:
            n = self.head 
            while n.data != value:
                n = n.next
            new_node.next = n.next
            n.next = new_node
            new_node.prev = n
            n = n.next
            n.prev = new_node

    def del_begin(self):
        if self.head is None:
            print("What you want to delete your linked list already empty")
        else:
            self.head = self.head.next

    def del_end(self):
        if self.head is None:
            print("What you want to delete your linked list already empty")
        else:
            n = self.head
            i = 1
            while n.next is not None: # this loop is for finding index of last element
                n = n.next
                i +=1
            j = 1
            n = self.head
            while True: # this loop run till 2nd last element and that we give refernce of 2nd last element to None
                if j == i-1 :
                    n.next = None
                    break
                else:
                    j += 1
                    n = n.next
            

    def del_by_value(self,value):
        pass

    def add_first_node(self,data): # This function for add First Node
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("Your Linked List Is Not empty so it means Nodes are present\n\n So  we Can not add Your Given Node")



DLL = Doubly_Linked_List()
DLL.add_first_node(1)
DLL.add_begin(5)
DLL.add_begin(10)
DLL.add_begin(15)
DLL.add_end(20)
DLL.add_before(50,5)
DLL.add_after(735,1)
DLL.del_end()
DLL.del_begin()
DLL.print_DLL()