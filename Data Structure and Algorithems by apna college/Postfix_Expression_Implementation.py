# ========= Postfix Epression Evaluation using stack========

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


# ========== Implementing postfix Expression
    

    def postfix_eva(self,list1):

        for i in range(len(list1)):

            if type(list1[i]) == int: #  here we move from left to right in list
                self.push(list1[i])
            else:
                operand1 = self.pop()
                operand2 = self.pop() 

                if list1[i] == "+":
                    x = operand2 + operand1   
                    self.push(x)
                elif list1[i] == "-":
                    y = operand2 - operand1
                    self.push(y)
                elif list1[i] == "*":
                    z = operand2 * operand1
                    self.push(z)
                elif list1[i] == "/":
                    q = operand2 / operand1
                    self.push(q)




stack1 = Stack(5)

list1 = [4,6,"+",2,"/",5,"*",7,"+"]
list2 = [6,2,"*",1,"-",6,2,"/","+"]
stack1.postfix_eva(list2)
print(stack1.isEmpty())
stack1.print_stack()
