# ========= Array Challenges ==========

#Problem :
'''
Problem :
Given an array a[] of size n. For every i from 0 to n-1
output max(a[0],a[1]...a[i])

'''

# let 
'''
a = [2,3,45,76,12,34,735,0,34,7]
try:
    i = int(input(f"Enter number less then {len(a)} to find maximum till that index \n"))
    max_no = a[0] 
    for j in range(i): # complexity O(n)
        max_no = max(max_no,a[j])
        # if max_no < a[j]:
        #     max_no = a[j]

    print(f"Maximum Number till ith index is {max_no}")
except:
    print("Your index value out of range")
'''

# ======= Subarray VS Subsequences =========

'''
--> Subarray - Continous part of  the array.
--> Number of subarrays of an array with n elements = nC2 +n = n*(n+1)/2

'''

'''
--> A subsequence is a sequence that can be derived an array by selecting zero or more 
    elements , without changing the order of the remaining elements.
--> Number of subsequences of an array with n elements = 2^n. # here we take zero also

'''

# Every Subarray is a Subsequence but every Subsequence is not Subarray.

# Problem :
'''
Problem:

Sum of All SubArrays.

    Given an array a[] of size n.Output sum of each subarray of the given array. 

'''
# a = [1,2,2]
# # sub array of this is --> 1 1,2 1,2,2 2 2,2 2
# sub_array = []

# def subarray(array):
#     j = 0
#      # we make list b for nested list
#     while(j<len(array)):
#         b = []
#         for i in array[j:]:
#             b.append(i)
#             sub_array.append(b)
#         j = j + 1
    

# subarray(a)
# print(sub_array)
'''
a = [1,2,0,7,2]
sum_list= []
for i in range(len(a)):
    for j in range(i,len(a)):
        if i == j:
            sum= a[i]
            sum_list.append(sum)
        else:

            sum = sum + a[j]
            sum_list.append(sum)

print(sum_list)
'''

# Problem :
'''
Problem :
       Longest Arithematic Subarray

'''
'''
t1 = [11,12,13,14,15,16,17,18,1,2,3,4,5,6,7,8,9,2,2,2,2,2,2,2,2,2,2,2,2]
t2 = [1,2,3,4,5,5,555,4,4,4,4,4]
t3 = [90,89,88,87,86,85,84,23,24,25,2,2,2]
t4 = [10,7,4,6,8,10,11]
# a = [3,4]
# Here we determine the length of the longest conigous arithmetic subarray

def Longest_AA(array):
    list_count =[]
    i = 0
    j = 1
    count = 1
    diff = array[1] - array[0]
    while(j<len(array)):
        if diff == array[j] - array[i]:
            count += 1
            list_count.append(count)
        else:
            list_count.append(count)
            count = 2
            diff = array[j] - array[i]    
        i = i + 1
        j = j + 1 
    print(list_count)
    return max(list_count)

count=Longest_AA(t1)
print(f"testcase1: Longest Arithematic Array count is {count}")
count=Longest_AA(t2)
print(f"testcase2: Longest Arithematic Array count is {count}")
count=Longest_AA(t3)
print(f"testcase3: Longest Arithematic Array count is {count}")
count=Longest_AA(t4)
print(f"testcase4: Longest Arithematic Array count is {count}")
'''

#  Problem:
'''
Record Breaker:

# The number of visitors on the day is strictly larger then the number of visitors on each 
 of the previous days.

# Either it is the last day , or the number of visitors on the day is strictly larger than 
 the number of viitors on the following day.

Note : Note that the very first day could bea a record breaking days 

'''

a = [1,2,0,7,2,0,2,2]


count = 0
if len(a) == 1:
        count = 1
else:
    a.append(0)    
    j = 1 
    while(j-1<len(a)-1): # complexity is O(n)
        if a[j-1] == max(a[:j]) and a[j-1]>a[j]:
            count += 1
        j = j + 1
print(a)
print(f"Number of record breaking days is {count}")


            

