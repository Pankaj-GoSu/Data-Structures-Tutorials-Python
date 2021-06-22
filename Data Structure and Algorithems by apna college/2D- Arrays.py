#====== Two Dimentional Arrays ==========

# Declaring a 2D array .

'''
row_size = int(input("enter row size of 2D array."))
column_size = int(input("enter column size of 2D array."))

array_2d = []
array = []
for i in range(row_size):
    for j in range(column_size):
        val = int(input("Enter value to array"))
        array.append(val)
    array_2d.append(array)
    array = []
# print(array_2d)

for i in range(len(array_2d)):
    for j in array_2d[i]:
        print(j, end = " ")
    print()

'''

# Problem

'''
Searching a Matrix :
array_2d = [[1,2,3,],[4,5,67],[23,6,8]]
search : 67

'''
'''
array_2d = [[1,2,3,],[4,5,67],[23,6,8]]
s =  9
flag = False
for i in range(len(array_2d)):
    for j in  range(len(array_2d[i])):
        if array_2d[i][j] == s:
            flag = True
            print(f"Coordinates of key : {i} , {j}")
           

if flag:
    print("Your key is present")
else:
    print("You key is not found")

'''

# Problem : 

'''
Spiral Order Matrix Traversal:

'''
array_2d = [[1,2,3,],[4,5,6],[7,8,9]]

row_start = 0
row_end = 2
column_start = 0
column_end = 2

def Spiral_Traversal(array,row_start,row_end,column_start,column_end):

    if row_start == row_end == column_end == column_start:
        print(array[row_start][row_end])
        return
    else:
        for i in range(column_start,column_end+1):
            print(array[row_start][i])
        row_start = row_start + 1
        for j in range(row_start,row_end+1):
            print(array[j][column_end])
        column_end = column_end - 1
        for k in range(row_start,column_end+1):
            print(array[row_end][column_end-k+1])
        row_end = row_end - 1
        for l in range(column_start,row_end+1):
            print(array[row_end - l +1][column_start])
        column_start = column_start + 1
    
    Spiral_Traversal(array,row_start,row_end,column_start,column_end)




Spiral_Traversal(array_2d,0,2,0,2)
        

