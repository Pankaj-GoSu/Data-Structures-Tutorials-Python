#========== Problems which are asked in Top MNC's ============

# Problem :
'''
First Repeating elements:
input -> 1,5,3,4,3,5,6
output -> 2
Explanantion->
5 is apprearing twice and its first appearance is at index 2 which is less than 3 
whose first occurring index is 3.

'''

'''
a = [2,2,3,4,3,5,6]

j = 0

while(j<len(a)):
    for k in range(j+1,len(a)):
        if a[j] == a[k]:
            print(f"first repeating index is {j}")
            exit()
    j = j + 1

'''

# Problem :

'''
Given an unsorted array A of Size of N od non-negative integers,find a continous subarray 
which adds to a given numders S.

Input:
N = 5 , S = 12
A= [1,2,3,7,5]

Output: 2 4 
Explanation: The sum of element from 2nd postion to 4th postion is 12.

'''

'''
A = [1,2,3,7,5]
sum_list = []
S = 7
sum = 0
for i in range(len(A)):
    for j in range(i,len(A)):
        sum = sum + A[j]
        sum_list.append(sum)
    sum = 0
print(sum_list)
'''
# a = [-1,4,7,2]

# ========== Solution ==============

a = [1,2,3,7,5]
S = 17
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
sum = 0
for i in range(len(sub_array)):
    for j in range(len(sub_array[i])):
        sum = sum + sub_array[i][j]
    if sum == S:
        x = sub_array[i]
    sum = 0

st = a.index(x[0])
en = a.index(x[-1])
print(f"Starting index is : {st} end index is : {en}")
print(x)

# Problem :

'''
Smallest Positive Missing Numbers :

You are given an array of N integers including 0.The task is to find the smallest positive number 
missing from the array.

'''

'''
a = [0,-9,1,3,-4,5]

i = 0
j = max(a)
while True:
    if i <= j:
        if i in a:
            pass
        else:
            print(f"smallest positive number which is missing is {i}")
            break
        i = i + 1
    else:
        print("no number is missing")
        break
'''
