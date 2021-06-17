#============= Here i write Code for Deletion Operation in graph =========

'''
1-Function to delete a node using adjacency matric representation.
2-Function to delete an edge using adjacenct matrix representation.
3-Function to delete a node using adjacency List representation.
4-Function to delete an edge using adjacenct List representation.

'''

#======== First we copy code of graph which include node and edge.==========


nodes = []
adjacency_matrix_graph=[]

def add_node(node): # this function work fine for all graph weather directed undirected weighted or unweighted
    temp=[]
   
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


def add_edge(v1,v2,cost): # it take edge as a arguments.

    # if v1 and v2 not in nodes:
    #     print(" Node is not present")
    if v1 not in nodes:
        print(f"{v1} is Not present")
    elif v2 not in nodes:
        print(f"{v2} is Not present")
    
    else:
            
             
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)

        adjacency_matrix_graph[index_v1][index_v2] = cost
        adjacency_matrix_graph[index_v2][index_v1] = cost

print("After Adding Edge \n") 

add_edge("F","G",1)
add_edge("F","H",1)
add_edge("G","H",1)
add_edge("G","K",1)

print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)


#===========1-Function to delete a node using adjacency matric representation.===========

def deletion(node):
    if node not in nodes:
        print("\n Which Node You want to delete it is not present in graph\n")
        return
    else:
        index_node = nodes.index(node)
        del nodes[index_node]
        for i in range (len(adjacency_matrix_graph)):
            del adjacency_matrix_graph[i][index_node] 
        del adjacency_matrix_graph[index_node]

# deletion("G")

print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)


#========= 2-Function to delete an edge using adjacenct matrix representation.======

def Delete_Edge(v1,v2):

    if v1 not in nodes:
        print(f"{v1} vertex is node present")
    elif v2 not in nodes:
        print(f"{v2} vertex is node present")

    else:
        index_v1 = nodes.index(v1)
        index_v2 = nodes.index(v2)
        adjacency_matrix_graph[index_v1][index_v2] = 0
        adjacency_matrix_graph[index_v2][index_v1] = 0


Delete_Edge("F","G")

print(nodes)
print(adjacency_matrix_graph)
print_in_matrix(adjacency_matrix_graph)
