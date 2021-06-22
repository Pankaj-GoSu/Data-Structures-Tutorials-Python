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
# a =[-1,-1,-1,-1]
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
# A = [-1,4,7,2]
A = [-1,-1,-1,-1]
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
# array = [-1,4,7,2]
array = [-1,-1,1,-1]  # this algo not working for input with all negative numbers or 0 included with negative numbers.
current_sum = 0
maxsum = array[0]

for item in array: # time complexity is O(n) 
        current_sum = current_sum + item
        if current_sum < 0:
            current_sum = 0
        if current_sum > maxsum:
            maxsum = current_sum
print(f"maximum subarray sum is : {maxsum}")
'''





#Problem :

'''
Maximum Circular Subarray Sum:

'''

'''
# a = [4,-4,6,-6,10,-11,12]
# a = [-1,4,-6,7,5,-4]
# Here we find not contributing or not wraping elements and then ae add complete array
# after that we substract not contrributing elements 

Max subarray sum = Total sum of array - sum of non-contributing elements.

'''

'''
# a = [4,-4,6,-6,10,-11,12]
a = [-1,4,-6,7,5,-4]

max_sum = -a[4]
current_sum = 0
for i in a: # It is sum of non-contributing elements 
    current_sum = current_sum + (-i)
    if current_sum < 0 :
        current_sum = 0
    if current_sum > max_sum:
        max_sum = current_sum
    
print(max_sum)
total_sum = 0
for i in a : # Total sum of element
    total_sum = total_sum + i
print(total_sum)
print(f"Max Circular Subarray Sum is : {total_sum - (- max_sum)}  ")
'''

# Problem :

'''
Pair Sum Problem :

Check if there exits two elements in an array such that their sum is equal to given k.

array = [2,4,7,11,14,16,20,21]
k = 31
it return True because sum of 11 + 20  is 31

'''

'''
array = [2,4,7,11,14,16,20,21]
k = 31
sum_list = []
for i in range(len(array)): # time complexity O(n):
    for j in range(i+1,len(array)):
        sum = array[j] + array[i]
        sum_list.append(sum)
        # if array[j] + array[i] == k:
        #     print("True")

print(sum_list)

if k in sum_list:
    print("True")
else:
    print("False")

'''


# We can do this by another method where time complexity is O(n).
# we can apply this method on sorted array.

array = [2,4,7,11,14,16,20,21]
i = 0 
j = len(array) - 1
k = 31

for x in range(len(array)): # here time complexity is O(n).
    if i >= j:
        print("False")
        break
    if array[i] + array[j] == k:
        print("True")
        break
    if array[i] + array[j] > k:
        # i = i
        j = j - 1
    if array[i] + array[j] < k:
        i = i + 1
        # j = j

