# ======= 7 Best Problems on Recursion =======

#Problem:

'''
Reverse a string using recursion
'''
str ="imawsog jaknap"

'''
def Reverse_str(str,i):

    if i == len(str):
        return 
    else:
        Reverse_str(str,i+1)
        print(str[i],end ="")
    
    return 
        

        
Reverse_str(str,0)
# print(x)
'''

#Problem :

'''
Replace pi with 3.14 in string
input =>> "pippxxppiixipi"
output =>> "3.14ppxxp3.14ixi3.14"

'''
'''
str = "pippxxppiixipi"

def Replace_pi(str,key,i):

    if i == len(str)-1:
        return
    else:
        if str[i:i+2] == key:
            str=str.replace(str[i:i+2],"3.14")
            return str
        Replace_pi(str,key,i+1)
        
    
key ="pi"
print(Replace_pi(str,key,0))

'''

#Problem :

'''
Tower of Hanoi
'''

'''
def TOH(a,b,c,n):

    if n == 1:
        print(f"Move disc from {a} to {c}")
    else:
        TOH(a,c,b,n-1)
        print(f"Move disc from {a} to {c}")
        TOH(b,a,c,n-1)

TOH("source","helper","destination",3) # it print 2^n -1 times

'''

#Problem

'''
Remove all duplicates from the string.

input =>> aaaabbbeeecdddd
output =>> abecd 
'''
'''
x =" "

str = "aaaabbbeeecdddd"

def duplicateremove(str,x,i):
    
    if i == len(str) - 1:
        return
    else:
        if x == str[i]:
            duplicateremove(str,x,i+1)
        else:
            print(str[i],end = "")
            x = str[i]
            duplicateremove(str,x,i+1)

duplicateremove(str,x,0)
'''

#Problem

'''
Move all x to the end of the string
input =>> "axxbdxcefxhix"
output =>> "abcdefhixxxxx"

'''

'''
str = "axxbbdxcefbxhix"
def move_x(str,i ,x):
    global str1
    global str2
    if i == len(str):
        return
    else:
        if str[i] == x:
            str1 = str1+str[i]
            move_x(str,i+1,x)
            
            
        else:
            str2 = str2 + str[i]
            move_x(str,i+1,x)
            
    return str2+str1
str1 = ""
str2 = ""
x = "x"

print(move_x(str,0 ,x))

'''

# Problem:

'''
Generate all substrings of a string:
"ABC"  ==> {"",A,B,AB,C,,AC,BC,ABC}

'''
# here we do this by input ouput method.

str = "ABC"
out = ""

def substrings(str,out,i):

    if len(str)==i:
        print(out)
        return out
    else:
        op1 = out
        op2 = out
        op2 = op2 + str[i]
        substrings(str,op1,i+1)
        substrings(str,op2,i+1)
        
substrings(str,out,0)
