#=============== Set and Dictionary (Data Structures) =================

s = set("Hello")
print(s)

# set is collection of unique values,Dublicated are ignore

s = {1 , 2 ,3 ,5}

print(s)

# Set is  unorderd

a = {1,2,3,4}
b = {3,2,1,4}
print(a==b) # it return True

# set is mutable
s.add(4)
print(s)

# set can contain only unmutable element 
# so list is not element of set

# s = {[3,4],5} # it give error

# Set is Not nested beacuse set is mutable and it not take mutable elements as arguments.
'''
To access elements of set data type we need loop because it does not have key , 
and we also not access it by index because sets are unorderd
'''
# print(1 in s)
x = 1 in s
print(x)

