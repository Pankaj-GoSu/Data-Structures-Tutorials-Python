#=============== Deleting elements from Linked List =================

# =========== Here I focused in concept so i take ideal cases not handel error =========

'''
We can Delete Elemets at different places
1- Begining --> del_begin()
2- End --> del_end()
3- In Between By Index and Value of node --> del_by_value(self,value)

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

    def del_begin(self):
        """ Deleted Begin node of Linked List"""
        self.head =self.head.ref # directly We change head position so automatically Node deleted from Linked list

    def del_end(self):
        """ Deleted end Node of LinkedList"""
        n = self.head
        i = 1
        while n.ref is not None: # this loop is for finding index of last element
            n = n.ref
            i +=1
        j = 1
        n = self.head
        while True: # this loop run till 2nd last element and that we give refernce of 2nd last element to None
            if j == i-1 :
                n.ref = None
                break
            else:
                j += 1
                n = n.ref
    
    def del_by_value(self,value):
        n = self.head # give value of pointer head to n so that we can traversal by n without cahnging head position.
        i = 1
        while n.ref is not None : # This loop is for index of that perticular node which value is given.
            if n.data == value:
                break
            else:
                n = n.ref
                i += 1         
        
        j = 1
        m = self.head
        while True:
            if i == 1:
                self.del_begin()
                break
            elif j == i-1: # here we change reference of node which is before(m) the given node to next node of given node(n) 
                m.ref = n.ref 
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
LL1.after_node(15,100) # enter or add 15 after value 100.
LL1.before_node(25,20) # enter or add 25 before value 20.
# LL1.del_begin()
# LL1.del_end()
LL1.del_by_value(25)
LL1.del_by_value(20)
LL1.print_LL()



