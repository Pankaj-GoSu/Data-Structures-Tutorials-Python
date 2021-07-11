#============ Heap Introduction=======

'''
it is basically a complete binary tree:
we have 2 heaps 
Max heap: Root > rest of the elements present in its subtree and it apply on every node. 
Min heap: Root < rest of the elements present in its subtree and it apply on every node. 

'''

# How to Convert an array into a MaxHeap:

# ===== Heapq module ======
'''
Heapq is python module it provides the implementation of min heap.
and provide many operaations.
'''

import heapq

'''
heapq.heappush(heap(list),item) : push item onto heap,maintaining the heap property.

'''
heap = []
heapq.heappush(heap,10)
print(heap)
heapq.heappush(heap,1)
print(heap)
heapq.heappush(heap,5)
print(heap)

'''
heapq.heapop(heap(list name))
 ==> will return the smallest value and also it will delete that from heap , maintaining
     the heap property.
'''

a = heapq.heappop(heap) # it return min value and delete that value also or it remove root node.
print(a)
print(heap)


'''
heapq.heapify(heap(list name)) :
it convert a given list to a binary heap or binary min heap.
'''

list1 = [1,3,5,2,4,6] # it is a simple list.
heapq.heapify(list1)
print(list1)

'''
heapq.heappushpop(heap(list name),item) : first it push item by maintaing the heap property and then
                    it return the smallest value from the heap and also delete that element.
'''

b = heapq.heappushpop(list1,89)
print(b)
print(list1)

'''
heapq.heapreplace(heap,item) : first it pop the smallest element then it insert the new element.
'''

c = heapq.heapreplace(list1,100)
print(c)
print(list1)

'''
heapq.nsmallest(n,iterable(list),key = None)
'''
heap1 = [1,20,5,4,3,6,2]
a= heapq.nsmallest(2,heap1) # it give 2 smallest number.
print(a)

'''
heapq.nlargest(n,iterable(list),key = None)
'''
x = heapq.nlargest(3,heap1)
print(x)


#========= To implement priority queue using this heapq module =============

list1 = [(1,"ria"),(4,"sia"),(3 ,"gia")]

heapq.heapify(list1)
print(list1)

for i in range(len(list1)): # which has lowest value it has height priority.
    print(heapq.heappop(list1))
