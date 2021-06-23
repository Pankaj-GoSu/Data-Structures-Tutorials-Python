# ======= Recursion Challenges =============

#Problem:

'''
Check if an array is sorted or not.
'''

'''
array = [1,2,4,5,6]
a = False
for i in range(len(array)-1):
    if array[i+1]>array[i]:
        a = True
    else:
        a = False
        break

if a:
    print("Sorted order")
else:
    print("not in sorted order")  

'''

'''
array = [1,3,4,5,9,8]
def check_sort(array,i,j):

    if i == j - 1:
        print("Sorted Array")
    else:
        if array[i+1] > array[i]:
            check_sort(array,i+1,j)
        else:
            print("Array is not sorted")
        
            
            
check_sort(array,0,len(array))

'''

#Problem :

'''
Print numbers till n:

1- Decreasing order
2- Increasing order
'''

# Decreasing order:
'''
def decreasing(n):

    if n == 0:
        return
    else:
        print(n , end =" ")
        decreasing(n-1)

decreasing(5)
'''
# Increasing order:
'''
def increasing(n):

    if n == 0:
        return
        
    else:
        increasing(n-1)
        print(n, end =" ")
        

increasing(5)
'''

#Problem:

'''
Find the first and last occurence of a number in an array:
{4,2,1,2,5,2,7}
2 first occure at index 1 and last occure at index 5
'''

'''
a =[4,2,1,2,5,2,1,7]
count_list = []
count = 0
def occurence(a,num,count):
    
    if len(a) == 0:
        return
    else:
        if a[0] == num:
            count_list.append(count)
            a.pop(0)
            occurence(a,num,count+1)
        else:
            a.pop(0)
            occurence(a,num,count+1)

num = 2
occurence(a,num,count)
print(f"occurance of {num} is : start index {count_list[0]} and last index {count_list[-1]}")

'''
'''
a = [4,2,1,2,5,2,1,7]

num = 2
count = 0
def last_occur(a,i,num,count):

    if len(a) == count:
        return 
    
    if a[i] == num:
        last_occur(a,i+1,num,count+1)
        return count

    
        
x = last_occur(a,0,num,count)
print(x)


'''