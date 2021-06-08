#=========== Adding Elements after The given Node ============


#=========== First I write General Program =================
'''

  In This Program We Give index where we want to insert a node and we insert node at that point.

'''
'''

class Node:

    def __init__(self,data): #class constructor or initializtion method.
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None # it means we do not have any node because head is None(Null),It is a Empty Linked List.

    def print_LL(self): # Traversal Operation performed here
        if self.head is None :
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None :
                print(n.data,"-->" , end =" ")
                n = n.ref       

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        else:
            n = self.head
            while n.ref is not None :
                n = n.ref

            n.ref = new_node
              
    def in_Between_add(self,data,index): #index is where you want to insert node.
        new_node = Node(data)
        i = 1
        n = self.head
        while True:
            if i == index - 1 :
                new_node.ref = n.ref 
                n.ref = new_node
                break
            else:
                i += 1
                n = n.ref
    


LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
LL1.in_Between_add(50,2)
LL1.in_Between_add(50,4)
LL1.add_end(100)
LL1.add_end(30)
LL1.print_LL()

'''
#========== Now Program for Adding Node after a perticular Node ================



class Node:

    def __init__(self,data): #class constructor or initializtion method.
        self.data = data
        self.ref = None


class LinkedList:

    def __init__(self):
        self.head = None # it means we do not have any node because head is None(Null),It is a Empty Linked List.

    def print_LL(self): # Traversal Operation performed here
        if self.head is None :
            print("Linked List is empty!")
        else:
            n = self.head 
            while n is not None :
                print(n.data,"-->" , end =" ")
                n = n.ref       

    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        
        else:
            n = self.head
            while n.ref is not None :
                n = n.ref

            n.ref = new_node
              
    # With this function we add Node where we want to add by giving Index.
    def in_Between_add(self,data,index): 
        new_node = Node(data)
        i = 1
        n = self.head
        
        while True:
            if index == 1:
                new_node.ref = n
                self.head = new_node
                break
            elif i == index - 1 :
                new_node.ref = n.ref 
                n.ref = new_node
                break
            else:
                i += 1
                n = n.ref
    
    
    def after_node(self,data,value):
        ''' After which node value you want enter your new node'''
        new_node = Node(data)
        i = 1
        n = self.head
        while True :
            if n.data == value:
                new_node.ref = n.ref
                n.ref = new_node
                break
            else:
                i += 1
                n = n.ref

    def before_node(self,data,value):
        '''Before which node value you want enter your new node'''
        new_node = Node(data)
        i = 1
        j = 1
        n = self.head
        while True :
            if n.data == value:
                break
            else:
                i += 1
                n = n.ref
        m = self.head
        while True:
            if i == 1 :
                new_node.ref = m
                self.head = new_node
                break
            elif j == i-1:
                new_node.ref = m.ref
                m.ref = new_node
                break
            else:
                j += 1
                m = m.ref

LL1 = LinkedList()
LL1.add_begin(10)
LL1.add_begin(20)
# LL1.in_Between_add(50,1)
# LL1.in_Between_add(60,2)
LL1.add_end(100)
LL1.add_end(30)
LL1.after_node(15,100)
LL1.before_node(25,20)
LL1.print_LL()

