#=========== Priority Queue =====================

# Queue is linear data structure which work on FIFO methodology.
# Priority Queues are modified version of Queues in which 
# each element is assocaited with a priority and it servecs a/c to priority.
# In priority queue removal of element based on priority.

'''

 How to set priority :
 1- Value of that element is consider as priority .
   1.1 here we give lowest value to high priority.
   1,2 or we can give highest value to high priority.
 2- We can give priority and value in a tuple.

 '''

#  Example : # Here We take lowest value as high priority.

q = []

q.append(10)
q.append(20)
q.sort()
q.append(5) # user think out queue is q = [10,20,5]
q.sort()   # But actual queue is q =[5,10,20] So here we say lowest value has high priority.
print(q)

q.pop(0) # it pop 0 index value
print(q) # lowest value element removed 

# ====== Best way to implement priority Queue is using binary heap Data Structures ========

import queue

q = queue.PriorityQueue() # creat a empty queue. q is object of class PriorityQueue.
# here it take lowest value as high priority

q.put(10)
q.put(60)
q.put(30)
q.put(5)
q.put(5)

q.get() # 5 removed first 
q.get() # second 5 which is enter after 5 removed
q.get() # 10 removed

# ============We can add priority as a tuple==========

q = [] 
#q.append(priority,value)
q.append((2,"GoSu")) 
q.append((4,"How are you ?"))
q.append((1,"Hi"))
q.sort(reverse = True) #For highest value priority reverse = True 
print(q)

q.pop(0) # highest value element pop first.
print(q) 