#======= Subarrays Questions ===========

'''
A Subarray is a contiguous part of an array

'''

#Problem :

'''
Print all possible subarrays of a array.

'''

'''
a =[]
size = int(input("Size of array you want \n"))
for i in range(size):
    val = int(input("enter Value of array\n"))
    a.append(val)
print(a)
# a = [-1,4,7,2]
sub_array = []
b = []
k = 0
while True:
    if k < len(a):
        for i in range(k,len(a)):
            for j in range(k,i+1):
                b.append(a[j])
            sub_array.append(b)
            b = []
        k = k + 1
    else:
        break

print(sub_array)

'''

# Problem :
'''
Maximum Subarray sum :
Find the subarray in an array which has maximum sum.

'''
'''
a = [-1,4,7,2]
k = 0
b = []
sub_array = []
while True:
    if k < len(a):
        for i in range(k,len(a)):
            for j in range(k,i+1):
                b.append(a[j])
            sub_array.append(b)
            b = []
        k = k + 1 
    else:
        break 

sum_list = []
sum = 0
for i in range(len(sub_array)):
    for j in range(len(sub_array[i])):
        sum = sum + sub_array[i][j]
    sum_list.append(sum)
    sum = 0

print(sub_array)
print(sum_list)
max_no = sum_list[0]
for item in sum_list:
    if item > max_no:
        max_no = item
# max_val = max(sum_list)
max_index = sum_list.index(max_no)

print(f"Subarray which has maximum sum is : {sub_array[max_index]}")

'''

'''
A = [-1,4,7,2]
sum_list = []
S = 7
sum = 0
for i in range(len(A)): # here time complexity is O(n^2)
    for j in range(i,len(A)):
        sum = sum + A[j]
        sum_list.append(sum)
    sum = 0
print(sum_list)

'''


# ========== Kadane's algorithem =============

'''
We use this algorithem to obatain maximum sum of array in O(n). 
--> Array [-1,4,-6,7,-4]
if current sum is negative make it 0.
current sum = 0 4 0 7 0
so here maximum sum of subarray is 7
'''

'''
array = [-1,4,7,2]
current_sum = 0
maxsum = array[0]
for item in array: # time complexity is O(n) 
    current_sum = current_sum + item
    if current_sum < 0:
        current_sum = 0
    if current_sum > maxsum:
        maxsum = current_sum
print(maxsum)

'''

#Problem :

'''
Maximum Circular Subarray Sum:

'''
# a = [4,-4,6,-6,10,-11,12]
# a = [-1,4,-6,7,5,-4]
a = [4,-4,6,-6,10,4,-4,6,-6]
for i in range(len(a)-1):
    a.append(a[i])

current_sum = 0
max_val = a[0]
for item in a:
    current_sum = current_sum + item
    if current_sum < 0:
        current_sum = 0
    if current_sum > max_val:
        max_val = current_sum

print(max_val)