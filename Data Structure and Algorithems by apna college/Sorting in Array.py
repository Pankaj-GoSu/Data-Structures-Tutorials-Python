#========== Sorting in Arrays =============

'''
--> Sorting is ordering the array elements in asceding order.

'''

#=============== Selection Sort ============:

'''
Find the minimum element in unsorted array and swap it with element at begining.
then index is not at 0 it become 1 because at 0 we have minimum element , then apply this for 
reaming array.

array - [12,45,23,51,19,8]
step1 - [8,45,23,51,19,12]
step2 - [8,12,23,51,19,45]
step3 - [8,12,19,51,23,45]
step4 - [8,12,19,23,51,45]
step5 - [8,12,19,23,45,51] # we get sorted array.

'''

# method 1

array = [12,45,23,51,19,8]
# This below code for selection sort : theory is correct.

def selection_sort(array,i): # It take array and i = 0 as index of first element.
    if i <= len(array) - 1 :
        min_no = array[i]
        for item in array[i:]:
            if item < min_no:  
                min_no = item
        j = array.index(min_no)            
        array[i],array[j] = array[j],array[i]
        i = i + 1
        selection_sort(array,i)
    

print("Before sorting array is :")    
print(array)
selection_sort(array,0)
print("After sorting array : method 1")
print(array)

# method 2

array1 = [12,45,23,51,19,8]

def selection_sort2(array): # this code is not for selection sort becoz here in we swap value many times.

    for i in range(len(array)-1): # i goes from 0 to n-1 and j goes from 1 to n.  
        for j in range(i+1,len(array)): # here index of y always +1 of index of i .
            if array[i] > array[j]:
                array[i],array[j] = array[j],array[i]

selection_sort2(array1)
print("After sorting array : method 2")
print(array1)


#===== Bubble Sort ==========

'''
Reapetedly swap two adjacent elements if they are in wrong order.

Hum ise bubble sort isliye kahte h qnki jo humara maximum element hota h wo bubble ki trh upar aa jata h.
'''

def Bubble_sort(array,n):
    i = 0
    j = 1
    if n == 1:
        return array
    else:    
        while(j < n): # here n is decreasing such that we not check last element after 1st sorting or after completion of one loop.
            if array[j]<array[i]:# here it is repeatedly swap when wrong order.
                array[i],array[j] = array[j],array[i]
            i = i + 1
            j = j + 1
        Bubble_sort(array,n-1)


array2 = [12,45,23,51,19,8]
Bubble_sort(array2,len(array2))
print(f"Bubble sort result : {array2}")


#======= Insertion Sort ==========

'''
Insert an element from unsorted array to its correct position in sorted array.

array- [12,45,23,51,19,8]
step-1 [12,45,23,51,19,8]
step-2 [12,23,45,51,19,8]
step-3 [12,23,45,51,19,8]
step-4 [12,19,23,45,51,8]
step-5 [8,12,19,23,45,51]

'''
# ======== This is sorting method by IBH ==========
# array3 = [12,45,23,51,19,8]

# def Insert(array,temp):
#     if len(array) == 0 or array[-1]<temp:
#         array.append(temp)
#     else:
#         temp1 = array[-1]
#         array.pop()
#         Insert(array,temp)
#         array.append(temp1)


# def Insertion_Sort(array):

#     if len(array) == 1:
#         return array
#     else:
#         temp = array[-1]
#         array.pop()
#         Insertion_Sort(array)
#         Insert(array,temp)

# Insertion_Sort(array3)
# print(f"Insertion sort result : {array3}")

# array3 = [12,45,23,51,19,8]

# def Insertion_sort(array):
#     i = 0
#     if len(array) == 1:
#         return array
#     while (i+1 < len(array)):
#         if array[i] > array[i+1]:
            
#         i = i+1

