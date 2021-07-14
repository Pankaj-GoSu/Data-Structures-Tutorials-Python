#============ Expedition(Expedi) ============

'''
Expedition means a long journey for a specific purpose.
'''

# another problem :
#======== Maximum and minmum Array Differnece ==========

'''
You are given an array , A of n elements . you have to remove exactly n/2 elements from array A 
and add it to another array B(initially empty)
Find the maximum and minimum values of difference between these two arrays.
we define the difference between these two array as:
summation of abs(A[i] - B[i]) .
'''
# abs function is used for absolute value.
x = -15
# print(abs(x))
# array must be in even number bcoz we have to devide it into 2 equal parts
array = [12,-3,10,0]
array.sort()
maximum_value = []
for i in range(int(len(array)/2)):
    maximum_value.append(abs(array[len(array)-1-i]) - array[i])
max_val = 0

for i in maximum_value:
    max_val = max_val + i

print(f"Maximum value {max_val}")

# ====== Minimum value=========
a = []
b = []
for i in range(len(array)):
    if i%2 == 0:
        a.append(array[i])
    else:
        b.append(array[i])
minimum_value = []
for i in range(len(a)):
    minimum_value.append(abs(a[i]-b[i]))
# print(minimum_value)

min_val = 0
for i in minimum_value:
    min_val = min_val + i
print(f"minimum value {min_val}")