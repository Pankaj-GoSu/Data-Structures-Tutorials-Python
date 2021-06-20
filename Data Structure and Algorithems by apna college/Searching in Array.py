#==== Searching in Arrays{Linear and Binary Searach} ======


# Linear search:

array = []
size = int(input("enter size of array\n"))

for i in range(size):
    array_values = int(input("Enter values for array\n"))
    array.insert(0,array_values)

key_to_search = int(input("enter what you want to search\n"))

print(array)

def linear_search(arr): # time complexity O(n)
    for index , item in enumerate(array):
        if item == key_to_search:
            return index
    return "not found"

print("Using linear search")
index = linear_search(array)
print(f"Which key you search it is {index} ")


# ====== Binary Search =======

# For binary search element in array are present in sorted manner asceding order :


# def binary_search(arr,key,start_index,end_index): # this function not return index .

#     mid = int ((start_index + end_index)/2) 

#     if key == arr[mid]:
#         print("Your key is present")

#     elif key > arr[mid]:

#         binary_search(arr,key,mid+1,len(arr))
#     elif key < arr[mid]:

#         binary_search(arr,key,0,mid-1)
    
    

def binary_search(array,size,key): #time complexity -> O(log n base2 )
    s = 0
    e = size

    while (s<=e):
        try:
            mid = int((s+e)/2)
            if key == array[mid]:
                return mid
            elif key > array[mid]:
                s = mid + 1
            elif key < array[mid]:
                e = mid - 1
        except:
            return " not found "
    


print("Using Binary Search")
index = binary_search(array,size,key_to_search)
print(f"Which key you search it is {index} ")

