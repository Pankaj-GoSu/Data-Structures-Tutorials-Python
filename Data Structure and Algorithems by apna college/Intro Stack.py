#======= Introduction to Stack ==========

'''
--> Stores a list of items in which an item can be added to or 
    removed from the list only at one end.

--> Linear Data Structure
--> Based on LIFO (Last in first out)
===>> Operations On Stack:
        push(x)
        pop()
        top()
        empty()
'''
# ========== Implementation of Stack =============

class Stack():

    def __init__(self,n):
        self.stack = []
        self.size = n
        self.top  = None

    def push(self,data):

        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.top = self.stack[-1]
    
    def pop(self):

        if not self.stack:
            print("Stack is already empty so no pop operation")
        else:
            self.stack.pop()
            if self.stack:
                self.top = self.stack[-1]

    def top_(self):

        if not self.stack:
            print("stack is empty")
        else:
            print(f"Your top most element is {self.top}")

    def isEmpty(self):

        if not self.stack:
            return True
        else:
            return False

    def print_stack(self):

        if not self.stack:
            print("stack is empty")
        else:
            print(f"Your stack is {self.stack}")


    
# size =int(input("enter sixe of stack you want"))

stack1 = Stack(5)

stack1.push(5)
stack1.push(9)
stack1.push(3)
stack1.push(7)
stack1.pop()
stack1.top_()
stack1.push(19)
stack1.top_()
stack1.pop()
stack1.top_()


print(stack1.isEmpty())
stack1.print_stack()
