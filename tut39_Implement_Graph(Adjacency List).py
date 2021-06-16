#==========Here We Implement Graph Using Adjacency List===========

#======= 3- Function to add a node using adjacency list representation.==========

# This is for any graph

graph ={}
# adjacency_list = []
def add_node(node):
    
    if node in graph:
        print("node is already in graph")
    
    else:
        graph[node] = []


add_node("A")
add_node("B")
add_node("C")
print("Before Adding  Add_Edge")
print(graph)

#======== 4- Function to add an edge using adjadency list representation. ==========
# This is for unweighted undirected graph
# we modifi it for weighted graph 

def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(f"{v1} is Not present")
    elif v2 not in graph:
        print(f"{v2} is Not present")
    else:
    # for node in graph:
    #     if v1 == node:
    #         list1 = graph[node]
    #         list1.append(v2)
    #         graph[node] = list1
    #     if v2 == node:
    #         list2 = graph[node]
    #         list2.append(v1)
    #         graph[node]= list2
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

print("After adding Add_Edge")

add_edge("A","C",10)
add_edge("A","B",5)
add_edge("D","A",3)
print(graph)
