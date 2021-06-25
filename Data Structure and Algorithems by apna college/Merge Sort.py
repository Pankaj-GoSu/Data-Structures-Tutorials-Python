# ========== Merge sort =============

'''
Merge sort use devide and conquer technique.
'''

a = [6,3,9,5,2,8,7,1]

def merge(arr,i,mid ,j):

    arr1 = [] # here we make two temp array to store value from 0 to mid and mid to len(arr) -1
    arr2 = []
    for k in range(i,mid+1): # using for loop we assign value to these empty arrays
        arr1.append(arr[k])
    for l in range(mid+1,j+1):
        arr2.append(arr[l])
   
    k = 0
    l = 0 
    i = i
    while(k < len(arr1) and l < len(arr2)): #here we compare bot arr1 element to arr2 element  
        if arr1[k] < arr2[l]:           # and update our original arr
            arr[i] = arr1[k]
            i = i + 1
            k = k + 1
        else:
            arr[i] = arr2[l]
            i = i + 1
            l = l + 1
    while(k<len(arr1)): # this loop run when "l" pointer reach to last of its array.
        arr[i] = arr1[k]
        i= i + 1
        k = k + 1
    
    while(l<len(arr2)): # this loop run when "k" pointer reach to last of its array but l is not at its last
        arr[i] = arr2[l]
        i = i + 1
        l = l + 1
def merge_sort(arr,i,j):

    if (i<j) :

        mid = int((i+j)/2)

        merge_sort(arr,i,mid)
        merge_sort(arr,mid+1,j)

        merge(arr,i,mid,j)
        
merge_sort(a,0,len(a)-1)
print(a)