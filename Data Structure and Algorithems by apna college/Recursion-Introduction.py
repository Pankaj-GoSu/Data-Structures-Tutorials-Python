#====== Recursion Introduction =========

'''
Function call itself to make problem smaller.

'''

#Problem 

'''
Sum till n = n + sum till n-1
'''

'''
def sum_n(n):

    if n == 1:
        return 1 # it return 1 to sum(2) becoz sum(1) is called by sum(2).
    else:
        return n + sum_n(n-1)
     
print(sum_n(2))

'''

#Problem :

'''
Calculate n raised to power of p.
'''
'''
def power(n,p):

    if p == 0:
        return 1
    else:
        return n * power(n,p-1)

print(power(3,2))
'''

# Problem:
'''
find the factorial of a number n

'''
'''
def factorial(n):

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))


'''

# Problem 

'''
Print the nth fibonacci Number:
'''

def fibonacci(n):

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))

