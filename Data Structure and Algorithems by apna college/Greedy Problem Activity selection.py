#======= Activity Selection Problem ===========

'''
Your are given n activities with their start and finish times ,
select tha maximum number of activities that can be performed by a single person,
assuming that a person can only work on a single activity at a time.

'''

# activity = [[10,20],[12,15],[20,30],[30,35]]

# count = 0
# x = 0
# j = activity[0][1]
# while True:
#     for i in activity:
#         if i[1] <= j:
#             j = i[1]
            
#     if x == j:
#         break

#     count = count + 1

#     for i in activity:
#         if i[0] >= j:
#             count = count + 1
#             x = j
#             continue

# print(count)

# activity = [[10,20],[5,7],[21,30],[11,35]]
# count = 1
# for i in activity:
#     for j in activity:
#         if i[1] == j[0]:
#             count = count + 1
#             break

# print(count)

# ======== Fractional Knapsack Problem ==========

item_with_price = [[40,5],[24,4],[30,6],[21,7],[12,6],[25,5],[35,5]]
W = 20
array = []
for i in item_with_price:
    x = i[0]/i[1]
    array.append(x)
maximum_value = 0
while True:
    y = max(array)
    index = array.index(y)
    array.pop(index)
   
    maximum_value = maximum_value + item_with_price[index][0]
    # print(item_with_price[index][0])
    W = W - item_with_price[index][1]
    
    if W < item_with_price[index][1]:
        # print(W)
        break
    item_with_price.pop(index)
item_with_price.pop(index)
y = max(array)
index = array.index(y)
array.pop(index)
print(W)
print(item_with_price[index][0]/item_with_price[index][1])
maximum_value = maximum_value + W*(item_with_price[index][0]/item_with_price[index][1])
print(maximum_value)

