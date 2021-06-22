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
