#======= Lsit Representaion of Binary Heap ==========

# Here we see how we represent binary heap tree as a list.

'''
# so to find element present at ith is list[i] 

-> if you want to find index of parent node and you know index of child node
    i.e. i then => (i-1)//2 , it give us index of paresnt of that node.

-> if you know index of parent i.e. i and want to find index of child :
    left child = (2*i) + 1
    right child = (2*i) + 2
'''


#============= Heapq module ============

'''
Heapq is a module of python and it provides the implementation of min heap and provides many functions

'''

import heapq
'''
# first function -> heapq.heappush(heap(list name),item)

Push item onto heap ,maintaining the heap property.
'''
heap = [] # blank list 
heapq.heappush(heap,10) # it make a min heap 
heapq.heappush(heap,5) # it make a min heap 
heapq.heappush(heap,2) 
print(heap)

'''
# second function -> heapq.heappop(heap(list name)):
        --> Will return the smallest value and also it will delete that from heap,
        maintaining the heap property.

'''
a = heapq.heappop(heap) #  it return the smallest value in heap.
print(heap,a)

'''
# third function ->heapq.heapify(heap(list name))
--> This function is convert a given list to binary min heap.
'''

list1 = [1,4,5,3,7,8,2]
heapq.heapify(list1) # it heapify our list1.
print(list1) # we get min binary heap tree.

'''
# fourth function-> heapq.heappushpop(heap(list name),item)

-->  it is combine action of "heappush" and "heappop" 
    Here it Push item onto heap ,maintaining the heap property.
    and Will return the smallest value and also it will delete that from heap,
        maintaining the heap property.

here first push then it pop.
'''

heapq.heappushpop(list1,89) # it return smallest value in the heap 
print(list1)

'''
# fifth function -> heapq.heapreplace(heap(list name),item)

--> first it pop the smallest element then it insert the new element

here first pop then push

'''

heapq.heapreplace(list1,100)
print(list1)

'''
# sixth function -> heapq.nsmallest(n,iterable(list name),key = None)

this function return n smallest no. in iterable. if n is 2 it give 2 smallest no.

'''
list2 =[5,6,8,2,3,41,3] # this is not binary heap tree

b = heapq.nsmallest(3,list2)  # it return 3 smallest no. from list and this function used any where not neccesary heap tree.
print(b)

'''
# seven function -> heapq.nlargest(n,iterable(list name),key = none)

'''
b = heapq.nlargest(3,list2)
print(b)

# =========== We can implenet priority queue ============

list1 = [(1,"ria"),(4,"sia"),(3,"jiya")]# smallest value has highest priority.


heapq.heapify(list1) # it make heap binary tree.
for i in range(len(list1)):
    print(heapq.heappop(list1))
