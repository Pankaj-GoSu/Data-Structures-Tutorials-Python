
# Linked List.

class Node:

    def __init__(self,data,next):
        self.data = data
        self.next = next


# We create Class Linked List Which Contain 
# Nodes and Head.

class LinkedList:

    
    def __init__(self):
        self.head = None

    def Add_Begin(self,data):
        node = Node(data,self.head)
        self.head = node
            

    def Add_End(self,data):
        n = self.head
        x = self.head.next
        while True:
            if n == None:
                node = Node(data,None)
                self.head = node
                break
            else:
                n = n.next
        
        self.head = x
     
    # def In_Between(data,index):
    #     i = 1
    #     n = self.head
    #     while True:

        
        
    
    def Print_LL(self):
        global list1
        if self.head is None:
            print("Linked List Is Empty")
        else:
            n = self.head
            while n is not None:
                print(f" Linked List Contain {n.data}")
                list1.append(f"{n.data}-->")
                n = n.next

        
list1 = []
LL1 = LinkedList()
LL1.Add_Begin(5)
LL1.Add_End(10)
LL1.Add_Begin(15)
LL1.Add_End(30)
LL1.Print_LL()
print(list1)
