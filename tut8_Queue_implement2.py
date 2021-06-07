# ============ Queue Implementation Using Classes os diffrent modules ==============

#============== 1 collections module --> class --> deque (double ended queue) ==========

'''
In deque class 

1- If you want to add data from right to left use "append method" and if you want to add data from
left to right use "appendleft method" 
2- If you want to remove item from left end use "popleft method" is you want to remove item from 
right side use "pop".

'''

# Example1 : Using here "appendleft" for adding and "pop" for removing so that it behave like queue(FIFO)
# Left to right data enqueue
import collections

queue = collections.deque() # it create a empty queue or we can say list.

# Adding value to queue 
queue.appendleft(5)
print(queue)
queue.appendleft(10)
print(queue)
queue.appendleft(15)
print(queue)

# Removing value from queue 

queue.pop()
print(queue)
queue.pop()
print(queue)


# Example2 : Using here "append" for adding and "popleft" for removing so that it behave like queue(FIFO)
#right to left data enqueue
import collections

queue = collections.deque() # it create a empty queue or we can say list.

# Adding value to queue 
queue.append(5)
print(queue)
queue.append(10)
print(queue)
queue.append(15)
print(queue)

# Removing value from queue 

queue.popleft()
print(queue)
queue.popleft()
print(queue)

# 2 queue module --> class --> Queue

# queue.queue(maximum size = 0 or less then 0) #  then it is a infinte queue.
# In queue class we have method to enqueue is put and put_nowait 
# For dequeue is get and get_nowait

import queue

q = queue.Queue() # by default max valuue is 0 means infinite queue.

q.put(10)
q.put(20)
q.put(30)

print(q) #q is a object of class Queue so it do not show q values it give only address where is object point

q.get()
q.get()

