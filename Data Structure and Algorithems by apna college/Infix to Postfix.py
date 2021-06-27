# ========= Infix to Postfix using stack ==============

# first we implement stack

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

#========= Implementing Infix to Postfix ========

    def infix_to_postfix(self,list1):

        for i in range(len(list1)):

            if type(list1[i]) == int:
                print(list1[i],end ="")
                
            else:
                if list1[i] == "(":
                    self.push("(")
                elif list1[i] == "/":
                    self.push("/")
                elif list1[i] == "*":
                    self.push("*")
                
                elif list1[i] == "+" or list1[i] == "-":
                    
                    if  len(self.stack) == 0: 
                        self.push(list1[i])

                    else:
                        if self.stack[-1] == "+" or self.stack[-1] == "-" :
                            self.push(list1[i])
                        else:
                            a = self.pop()
                            while a != "+" and a !="-":
                                print(a, end = "")
                                a = self.pop()
                            self.push(a)
                            self.push(list1[i])
                        

                elif list1[i] == ")":
                    while True:
                        a = self.pop()
                        if a=="(":
                            break
                        else:
                            print(a, end = "")
        while True:
            if len(self.stack) != 0:
                a = self.pop()
                print(a, end="")
            else:
                break
                   
                    
                        
st = Stack(15)

list1 = [5,"-",2,"*",3,"+",6]

st.infix_to_postfix(list1)
# st.print_stack()
print()
# print(len(st.stack))
# st.print_stack()