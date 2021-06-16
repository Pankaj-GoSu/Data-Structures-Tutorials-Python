#=========== Here We Implement Graph =============

#Here We Do:

'''
1-Function to add a node using adjacency matrix representation.
2-Function to add an edge using adjadency matrix representation.

3-Function to add a node using adjacency list representation
4-Function to add an edge using adjadency list representation.

'''
#1-Function to add a node using adjacency matrix representation.

# This code is for undirected Graph 
# In python to repersent values in matrix form we use nested list.

# nodes = ["A","B","C","D","E"]

# adjacency_matrix = [ [0,1,1,1,0] , [1,0,0,1,1] , [1,0,0,1,0] , [1,1,1,0,1] , [0,1,0,1,0] ]
nodes = []
adjacency_matrix_graph=[]

def add_node(node):
    temp=[]
    # for i in nodes:
    #     if i == node :
    #         print(f"This node already exist so we can not add this {i} node")
    #         exit()
    #     else:
    #         pass  
    if node in nodes: # if node in nodes then it return True.
        print(f"This node already exist so we can not add this node")  
    else:
        nodes.append(node)
        for i in range(len(adjacency_matrix_graph)):
            temp.append(0)
        adjacency_matrix_graph.append(temp)
        for i in range(len(adjacency_matrix_graph)):
            adjacency_matrix_graph[i].append(0)

def print_in_matrix(nested_list): # this function is to print in matrix form.

    for i in range(len(nested_list)):
        for j in nested_list[i]:
            print(j,end = " ")
        print()

add_node("F")
add_node("G")
add_node("H")
add_node("K")

print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)
