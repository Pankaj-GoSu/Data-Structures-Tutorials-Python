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

#========= Implementing prefix Expression =========
    
    def prefix_eva(self,list1): # it return evaluation of prefix expression. 

        for i in range(len(list1)-1,-1,-1): # here we move from right to left in list
            
            if type(list1[i]) == int:
                self.push(list1[i])
            else:
                operand1 = self.pop()
                operand2 = self.pop()
                
                if list1[i] == "+":
                    x = operand1 + operand2   
                    self.push(x)
                elif list1[i] == "-":
                    y = operand1 - operand2
                    self.push(y)
                elif list1[i] == "*":
                    z = operand1 * operand2
                    self.push(z)
                elif list1[i] == "/":
                    q = operand1 / operand2
                    self.push(q)
            

        


    


stack1 = Stack(10)
# stack1.push(10)
# print(stack1.pop())
list1 = ["-","+",7,"*",4,5,"+",2,0]
list2 = ["*",2,3]
list3 =["-","*",2,3,5]
list4 = ["-","+","/",6,2,3,2]
stack1.prefix_eva(list1)
# print(stack1.isEmpty())
stack1.print_stack()


# list1 = [1,2,"3"]
# for i in list1:
#     if type(i) == int:
#         print(i)