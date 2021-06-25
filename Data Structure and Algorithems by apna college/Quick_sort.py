# ============ Quick Sort ============

'''
Quick sort use devide and conquer technique.
--> Here we put a element into its correct position means before that element all are small but may 
or may not be sorted and after that element all are bigger but may or may not be sorted and then again we call
our function for small values and bigger values.

'''
arr = [2,3,1,5,4]
x = 1
y =len(arr)-1

def Quick_sort(arr,i,j):

    if (i<j):

        pi = pivot(arr,i,j,x,y)
       
        Quick_sort(arr,i,pi-1)
        Quick_sort(arr,pi+1,j)



def pivot(arr,i,j,x,y):
    pivot_el = arr[i]
    if x < y:
        for k in range(i+1,j):
            if pivot_el <= arr[k] and k <= j:
                break
            x = k
        for l in range(len(arr)-1,i,-1):
            if pivot_el >= arr[l] :
                break
            y = l
        arr[x],arr[y] = arr[y],arr[x]
        
        pivot(arr,i,j,x,y)
    
    arr[i],arr[y] = arr[y],arr[i]
    return y 
        
Quick_sort(arr,0,len(arr))
print(arr)