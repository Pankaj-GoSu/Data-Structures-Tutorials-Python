# ========== Prefix Expression Evaluation Using stack =============

#======= First we implement stack =====

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
            temp = self.stack[-1]
            self.stack.pop()
            if self.stack:
                self.top = self.stack[-1]
        return temp
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

#========= Implementinf prefix Expression =========
    def prefix_eva(self,list1):
        operand1 = None
        operand2 = None

        for i in list1:
            if i == int:
                self.push(i)
            
        
        
        
        


    


stack1 = Stack(10)

list1 = ["-","+",7,"*",4,5,"+",2,0]

stack1.prefix_eva(list1)
# print(stack1.isEmpty())
stack1.print_stack()


