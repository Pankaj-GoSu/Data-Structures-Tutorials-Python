#=========== Here We Implement Graph Using Adjacency matrix =============

#Here We Do:

'''
1-Function to add a node using adjacency matrix representation.
2-Function to add an edge using adjadency matrix representation.

3-Function to add a node using adjacency list representation.
4-Function to add an edge using adjadency list representation.

'''
#1-===========Function to add a node using adjacency matrix representation.=========================

# This code is for undirected Graph 
# In python to repersent values in matrix form we use nested list.

# nodes = ["A","B","C","D","E"]

# adjacency_matrix = [ [0,1,1,1,0] , [1,0,0,1,1] , [1,0,0,1,0] , [1,1,1,0,1] , [0,1,0,1,0] ]
nodes = []
adjacency_matrix_graph=[]

def add_node(node): # this function work fine for all graph weather directed undirected weighted or unweighted
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

print("Before Adding Edge \n")
print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)

#=================== 2-Function to add an edge using adjadency matrix representation.==============

# this is only for undirected and unweighted graph.
# for weighted graph add cost and where we give one give cost simple.
# in directed graph we can make directed weighted graph or directed unweighted graph same as undirected graph
   # here if we give add_edge(A,B) then matrix[A][B] = 1 or cost not matrix[B][A] =1 or cost simple .
   # it means it directed from A to B not From B to A.

def add_edge(v1,v2,cost): # it take edge as a arguments.

    # if v1 and v2 not in nodes:
    #     print(" Node is not present")
    if v1 not in nodes:
        print(f"{v1} is Not present")
    elif v2 not in nodes:
        print(f"{v2} is Not present")
    
    else:
            
        # for index,item in enumerate(nodes): # this for loop is for find index of given vertex/nodes.
        #     if item == v1:
        #         index_v1 = index
        #     if item == v2:
        #         index_v2 = index
        #     else:
        #         pass
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)

        adjacency_matrix_graph[index_v1][index_v2] = cost
        adjacency_matrix_graph[index_v2][index_v1] = cost

        # for i in range(len(adjacency_matrix_graph)):# With this two for loop we access matrix.
        #     for j in range(len(adjacency_matrix_graph[i])):
        #         if  i == index_v1 and j == index_v2:
        #             adjacency_matrix_graph[i][j] = 1
        #             adjacency_matrix_graph[j][i] = 1


print("After Adding Edge \n") 

add_edge("F","G",10)
add_edge("F","K",5)
add_edge("F","X",7) # here X is not present but i give X as a input so that i check my code.
print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)





