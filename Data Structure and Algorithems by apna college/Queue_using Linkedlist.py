#============= LinkedList Implementation of Queue ============


# ====== So here we make linkedlist class =====
# and we just show linked list is behaving like queue.

class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist_queue:

    def __init__(self):
        self.head = None

    def enqueue(self,data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
            new_node.next = None
        

    def dequeue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            self.head = self.head.next
    
    def print_queue(self):
        if self.head is None:
            print("Queue is empty")
        else:
            n = self.head
            while n != None:
                print(f"{n.data} <--",end= " ")
                n = n.next

    def peek(self):
        if self.head is None:
            print("Queue is empty")
        else:
            print(self.head.data)

    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False

q = Linkedlist_queue()
q.enqueue(10)
q.enqueue(7)
q.enqueue(1)
q.enqueue(4)
q.dequeue()
            
q.print_queue()
print()
q.peek()
print(q.isEmpty())