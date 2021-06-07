#============ Implement stack Using List ===============

#1 we can implement stack using list
#2 we can implement stack using modules

#When we using list as stacks:
# for push ---> append
# for pop ---> pop

# Example: Here Operation is performed in LIFO

'''
stack = [] # creating a blank list
stack.append(10) 
print(stack)
stack.append(20)
print(stack)
stack.append(23)
print(stack)

stack.pop()
print(stack)
stack.pop()
print(stack)

'''
# To check weather the list / stack is empty here we use.
# isEmpty ---> len(stack)==0 len function
# or use "not stack" if stack is empty is return True.
# To access last element of stack which is list here then use index mathod (Index of last element is -1)

# ================= Complete Program for stack =============

stack = []

def Push():
    if n == len(stack):
        print("Your Stack is Full !\n")
        
    else:
        element = input(" Enter what you want to push \n")
        stack.append(element)
        
def Pop():
    if not stack:
        print("Your Stack is already empty so no pop operation take place\n")
    else:
        stack.pop()

def Print():
    print(f"Your Stack is {stack}\n")

def Top():
    if not stack:
        print("Empty list so no Top element present\n")
    else:
        print(f"Top element of stack is {stack[-1]}\n")

def isEmpty():
    if not stack :
        print("Your Stack is Empty")
    else:
        print(f"Your stack is not empty it has {len(stack)} elements")

n = int(input("limit of stack")) 

while True :
    inp = input("Which operation You want to perform \n \n push(type --> push) , pop(type --> pop) , print(type -->print) , \n\n top(type --> top) isEmpty(type --> isEmpty) or you eant to quit(type --> quit)\n")
    if inp == "push":
        Push()     
    elif inp == "pop":
        Pop()
    elif inp == "print":
        Print()
    elif inp == "quit":
        break
    elif inp == "isEmpty":
        isEmpty()
    elif inp == "top":
        Top()
    else:
        print(f"You entered {inp} as input please check and enter again\n")
        continue