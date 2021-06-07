# ====== Queue Implementation Using List ===============

'''
 Implement queue in two ways
1 - list
2 - Modules

'''
# Queue Work in first in first out method.

# Enqueue : process of adding elements to queue.
# Dequeue : process of removing the element from the queue.

'''

Enqueue --> append method
Dequeue --> pop method -->list.pop(0)

'''
'''

# here insert from right to left <--
queue1 = []

queue1.append(10) #append work as enqueue
print(queue1)
queue1.append(20)
print(queue1)
queue1.append(30)
print(queue1)

queue1.pop(0) # pop(0) work as dequeue
print(queue1)
queue1.pop(0)
print(queue1)

# here insert from left to right -->

queue2 = []

queue2.insert(0,10)
print(queue2)
queue2.insert(0,20)
print(queue2)
queue2.insert(0,30)
print(queue2)

queue2.pop()
print(queue2)
queue2.pop()
print(queue2)

queue3 = []

print(not queue3) # it return True because queue2 is empty 

# To check element at rear side and front side we use index [-1] and [0] when data enter from right to left.

'''
# ================= Complete Program for Queue ==================

# Here I make 2 class for left to right and right to left because we can add value in any manner


queue1 = [] # Queue for Left to Right. 
queue2 = [] # Queue for right to left.

class Left_to_Right():
    

    def Enqueue(self,Element):
        queue1.insert(0,Element)
        
    def Dequeue(self):
        if not queue1 :
            print("Queue is Empty\n")
        else:
            queue1.pop()
    
    def Print(self):
        print(queue1)
        
class Right_to_Left():


    def Enqueue(self,Element):
        queue2.append(Element)
        
    def Dequeue(self):
        if not queue2 :
            print("Queue is Empty\n")
        else:
            queue2.pop(0)

    def Print(self):
        print(queue2)



while True :
    inp = input("\t \t What You want to access \t \n 1 -Left To Right Queue \t\n 2 -Right to Left Queue \n 3- Quit \n")
    if inp == "1" :
        var1 = Left_to_Right()
        inp1 = input("What You want to do 1.Enqueue 2.Dequeue 3.Display 4. Quit\n")
        if inp1 == "1":
            inp2 = input("Enter Element which you want to Enqueue\n")
            var1.Enqueue(inp2)
        elif inp1 == "2":
            var1.Dequeue()
        elif inp1 == "3":
            var1.Print()
        elif inp1 == "4":
            break
        else:
            print("check input\n")
            continue
       
    elif inp == "2":
        var1 = Right_to_Left()
        inp1 = input("What You want to do 1.Enqueue 2.Dequeue 3. Display 4. Quit\n")
        if inp1 == "1":
            inp2 = input("Enter Element which you want to Enqueue\n")
            var1.Enqueue(inp2)
        elif inp1 == "2":
            var1.Dequeue()
        elif inp1 == "3":
            var1.Print()
        elif inp1 == "4":
            break
        else:
            print("check input\n")
            continue
    
    elif inp == "3":
        break

    else:
        print("Please Check Inputs \n")
        continue