# ======= Stack Challenges ==========

#============ Reverse a Sentence using Stacks ===============


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

#============ Reverse a Sentence using Stacks ===============

    def reverse_sentance(self,s):
                
        list1 = s.split()
        for i in range(len(list1)):
            temp = list1[0]
            stack1.push(temp)
            list1.pop(0)
        
        sentance_list = []
        for i in range(len(self.stack)):
            a = stack1.pop()
            sentance_list.append(a)
        sentance2 = " ".join(sentance_list) #  with the help of join function we make strings
        return sentance2

# ============ Reverse a stack =========

    def reverse_stack(self):

        if len(self.stack) == 1:
            return self.stack
        else:
            temp = self.stack[-1]
            self.stack.pop()
            self.reverse_stack()
            self.stack.insert(0,temp)
            self.top = self.stack[-1]

    
# size =int(input("enter sixe of stack you want"))

stack1 = Stack(15)
stack1.push(1)
stack1.push(2)
stack1.push(3)
stack1.push(4)
stack1.push(5)
stack1.push(6)
stack1.push(7)
stack1.print_stack()
stack1.reverse_stack()
stack1.print_stack()
# sentance1= "Hey, how are you doing? whats going on"
# print(sentance1)
stack1.top_()

# print(stack1.isEmpty())
# stack1.print_stack()
# x = stack1.reverse_sentance(sentance1)
# print(x)



