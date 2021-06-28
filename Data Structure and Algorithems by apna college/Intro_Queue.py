# ========= Introduction to Queue data Structure ==========

'''
Stores a list of items in which an item can be inserted at one end and removed from the other end.

--> Here we follow first in first out (FIFO) 
===>> Operations:
        1- enqueue(x)
        2- dequeue()
        3- peek()
        4 - isEmpty()
'''

class Queue:

    def __init__(self,size):

        self.queue = []
        self.size = size
        self.front = None
        self.back = None

    def enqueue(self,data):
        if len(self.queue) <= self.size:
            self.queue.append(data)
            self.front = self.queue[0]
            self.back = self.queue[-1]
        else:
            print("Queue Overflow")
    
    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty so no dequeue operation")
        else:
            self.queue.pop(0)
            if len(self.queue) == 0:
                self.front = None
                self.back = None
            else:
                self.front = self.queue[0]
                self.back = self.queue[-1]

    def peek(self): # it five value of front element.
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.front)
    

    def isEmpty(self):

        if len(self.queue) == 0:
            return True
        else:
            return False

    def print_queue(self):
        if len(self.queue) == 0:
            print("Queue is empty")
        else:
            print(self.queue)

q = Queue(10)
q.enqueue(7)
q.enqueue(4)
q.enqueue(5)
q.print_queue()
q.dequeue()
q.print_queue()
q.peek()
print(q.isEmpty())