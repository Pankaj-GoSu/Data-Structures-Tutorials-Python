#========== Problems which are asked in Top MNC's ============

# Problem :
'''
First Repeating elements:
input -> 1,5,3,4,3,5,6
output -> 2
Explanantion->
5 is apprearing twice and its first appearance is at index 2 which is less than 3 
whose first occurring index is 3.

'''

'''
a = [2,2,3,4,3,5,6]

j = 0

while(j<len(a)):
    for k in range(j+1,len(a)):
        if a[j] == a[k]:
            print(f"first repeating index is {j}")
            exit()
    j = j + 1

'''
