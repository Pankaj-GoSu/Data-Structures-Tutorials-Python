#============= Greedy Algorithm ===============

'''
At present, jo best lage wo le lo.

Markov Process : Process which depends only on the previous state.
'''

# General things to remember in Greedy Technique 
'''
--> Generally , sorting is done first while applying greedy technique.
'''

# Basic Problem of Greedy Algo:

# ==> Indian coin Change Problem:

array = [2000,500,200,100,50,20,10,5,2,1]
x = 355
count = 0

for i in array:
    count = count + int(x/i)
    x = x- int(x/i)*i # int(x/i)*i it give us integer value which is less then x. here x is updated.

    
print(count)




