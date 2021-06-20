#============ Introduction to Arrays ========

'''
-->Array is a list of variables of similar type.

-->1 int variable is equal to 4 bytes. 

--> We use index to acces array variables. indexing start with 0

'''

list = [10,20,30,40] # array becouse simlar type variables.

'''
input_for_array = input("enter numbers")
array = input_for_array.split() # The split() method splits a string into a list.
print(array)
'''

# array = []
# input_size = int(input("size of array"))
# for i in range(input_size):
#     input_for_array = int(input("enter number"))
#     array.insert(0,input_for_array)

# print("Your array is :")
# print(array)


# Question: Take a array from user and print maximum and minimum value of array:

array = []
size = int(input("Enter size of array"))

for i in range(size):
    array_values = int(input("Enter numbers: \n"))
    array.insert(0,array_values)

print("Your array is :")
print(array)
max_no = array[0]
min_no = array[0]
# for item in array:
#     if item > max:
#         max = item

#     if item < min:
#         min = item
for item in array:
    max_no = max(max_no,item)
    min_no = min(min_no,item)
    
print(f"Maximum value is {max_no} and minimum value is {min_no}")
