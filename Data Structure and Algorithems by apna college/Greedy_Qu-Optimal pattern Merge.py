#======== Optimal Pattern Merge ============

'''
here total cost is sum of all computation time
'''

computation_time = [5,2,4,7]
computation_time.sort() # to calculate minimium cost we just sort the arrat so that cost get minimized.
print(computation_time)
cost_list = []

sum = lambda a,b : a+b # lambda function return expression.

while len(computation_time) != 1:
    x = computation_time[0] + computation_time[1]
    cost_list.append(x)
    computation_time.pop(0)
    computation_time.pop(0)
    computation_time.insert(0,x)

print(computation_time)
y = 0
for i in cost_list:
    y = y + i
print(f"Minimum cost is {y}")