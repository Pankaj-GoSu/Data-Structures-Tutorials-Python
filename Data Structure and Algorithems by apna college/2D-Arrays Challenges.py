# ============ 2D Array Challenges ==========

#Problem :

'''
Matrix Transpose:

'''
# this is for square matrix.
'''
a = [[1,2,3],[4,5,6],[7,8,9]]
at= []
b = [] # this array work as row in transpose matrix

for i in range(len(a)):
    for j in range(len(a[i])):
        if i > j:
            a[i][j],a[j][i] = a[j][i],a[i][j]
     
print(a)
'''

# This is for any matrix it give Transpose of that matrix.
'''
a = [[1,2,3],[4,5,6]]
at= []
b = [] # this array work as row in transpose matrix

j = 0
while (j < len(a[0])):
    for i in range(len(a)):
        b.append(a[i][j])
    at.append(b)
    b = []
    j = j + 1

print(at)

'''

#Problem 

'''
Matrix Multiplication:

'''

'''
A = [[1,2],[3,4]]
B = [[2,1],[2,1]]
mul = [[0,0],[0,0]]

# traversing row of A
for i in range(len(A)):
    # Traversing column of B
    for j in range(len(B[0])):
        #Traversing row of B
        for k in range(len(B)):
            mul[i][j] = mul[i][j] + A[i][k]*B[k][j] 

print(mul)
 
'''
'''
cars = ["Aston" , "Audi", "McLaren "]
print(list(enumerate(cars)))
'''



#Problem:

'''
Matrix Search:
When row and column of matrix is sorted.
'''
A= [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]

# s = 1
# for i in range(len(A)):
#     if s in A[i]:
#         print("your key is present")
#         break
# else:
#     print("Key is not present")

# So when array is sorted we observe that from top right corner and bottom left corner 
# used as our starting point to search. 

#Hum observe kringe ki jaha humare pass choice ho ki bade m jana h ya chote m .

def matrix_search(matrix,i,j,target):
    if i < len(matrix) and j < len(matrix[0]):
        if (matrix[i][j]==target):
            print("Key is Found")
            return True
        elif (matrix[i][j] < target):
            j = j + 1
            matrix_search(matrix,i,j,target)
        else:
            i = i - 1
            matrix_search(matrix,i,j,target)
    else:
        print("Key is not found")
    
matrix_search(A,3,0,5)



