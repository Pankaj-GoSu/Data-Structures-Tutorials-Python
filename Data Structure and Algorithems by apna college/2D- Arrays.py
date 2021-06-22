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
OR
Spiral Matrix Traversal :

'''

# a = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
a =[[1,2,3],[4,5,6],[7,8,9],[11,12,13]]

top = 0
down = 3
left = 0
right = 2
while(top <= down and right >= left ):
    #print top
    for i in range(left,right+1):
        print(a[top][i], end = " ")
    top = top + 1
    #print right
    for j in range(top,down+1):
        print(a[j][right], end = " ")
    right = right - 1
    #print down
    for k in range(right,left-1,-1):
        print(a[down][k], end = " ")
    down = down - 1
    #print left
    for l in range(down,top-1,-1):
        print(a[l][left], end = " ")
    left = left + 1


