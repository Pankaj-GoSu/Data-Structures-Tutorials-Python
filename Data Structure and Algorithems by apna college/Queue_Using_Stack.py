#============ Queue using Stack =============


#========= Here first we make a class of Stack ==========


class Stack_queue:

    def __init__(self,n):
        self.stack = []
        self.size = n
        self.front  = None

    def push(self,data):

        if len(self.stack) == self.size:
            print("Stack Overflow")
        else:
            self.stack.append(data)
            self.front = self.stack[0]
    
    def pop(self):

        if not self.stack:
            print("Stack is already empty so no pop operation")
        else:
            
            self.stack.pop(0)
            if self.stack:
                self.front = self.stack[0]
            

    def front_(self):

        if not self.stack:
            print("stack is empty")
        else:
            print(f"Your top most element is {self.front}")

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

stack1 = Stack_queue(5)

stack1.push(5)
stack1.push(9)
stack1.push(3)
stack1.push(7)
stack1.front_()
stack1.print_stack()
stack1.pop()
stack1.front_()
# print(stack1.isEmpty())
stack1.print_stack()

