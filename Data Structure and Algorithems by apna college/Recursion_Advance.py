#=========== Advanced Recursion Problem =========

#Problem
'''
Print all possible permutations of a strings.
'''

'''

string = "ABC"
out =""
def permutation_string(string,out):
    
    if len(string) == 0:
        print(out)
        return
    else:
        for i in range(len(string)):
            op = out + string[i]
            left_str = string[0:i]
            right_str = string[i+1:]
            ros = left_str + right_str
            permutation_string(ros,op)
    
        
permutation_string(string,out)

'''

#Problem

'''
Count the number of paths possible from start point to end point in gameboard.
-->> let we have to go from 0 to 3 then we have 4 ways.
'''
'''
def count_path(n):

    if  n == 1 :
        return 1
    else:
        return n-2 + count_path(n-1)

print(count_path(6))

'''

#Problem 

'''
Count the number of paths possible in a maze
maze is -> n*n
'''
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

maze_column = 4
maze_row = 4
x = maze_column + maze_row - 2

a = factorial(x)
b = factorial(x-(maze_row-1))
c = factorial(maze_row-1)

total_path = a/(b*c)

print(total_path)
'''

def total_path(m,n):
    
    if n == 1 or m == 1:
        return 1
    else:
        return total_path(m-1,n) + total_path(m,n-1)

print(total_path(4,4))