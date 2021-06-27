#=========== Infix to Prefix =========

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

# ========= Implementing Infix to Prefix =================

    def infix_to_prefix(self,list1):# it give us result from left to right but result is write this output in note book from right to left.

        for i in range(len(list1)-1,-1,-1):

            if type(list1[i]) == int:
                print(list1[i],end="")
            else:
                if list1[i] == ")":
                    self.push(")")
                elif list1[i] == "/":
                    self.push("/")
                elif list1[i] == "*":
                    self.push("*")
                elif list1[i] == "+" or list1[i] == "-":
                    if len(self.stack) == 0:
                        self.push(list1[i])
                    else:
                        if self.stack[-1] == "+" or self.stack[-1] == "-":
                            self.push(list1[i])
                        else:
                            a = self.pop()
                            while a != "+" and a != "-":
                                print(a,end = "")
                                a = self.pop()
                            self.push(a)
                            self.push(list1[i])
                
                elif list1[i] == "(":
                    while True:
                        if self.stack[-1] != ")":
                            a = self.pop()
                            print(a,end ="")
                        else:
                            break
        while True:
            if len(self.stack) != 0:
                a = self.pop()
                print(a, end="")
            else:
                break                    



st = Stack(20)

list1 = [5,"-",2,"*",3,"+",6]

st.infix_to_prefix(list1)
