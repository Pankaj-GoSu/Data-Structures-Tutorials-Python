# ============== Implement Stack using Modules =================

#=========== 1 - Collections Module --> class --> deque (used as stack) it is double ended queue.========

# Example :

import collections
stack = collections.deque()
print(stack)

stack.append(10)
stack.append(20) # append is push same as list
stack.append(30)

print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)

print(not stack) # it give us False because it is not empty.

# And check Top element Use Index[-1] same as list.

# ========= 2 Queue Module -->class --> LiFo Queue (using this we create stack)

# for push --> put
# for pop --> get method

#Example :
 
import queue

stack = queue.LifoQueue() # if we give here argument as 3 so it only take 3 values


stack.put(10) # using put we push in stack
stack.put(20)
stack.put(30)

print(stack)

stack.get() # using get we pop from stack
stack.get()

print(stack)