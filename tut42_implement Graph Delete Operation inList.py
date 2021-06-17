
#=========== 3-Function to delete a node using adjacency List representation. =============

# Here First We copy code of adjacenct list add node and add edge method. so that we can delete


graph ={}

def add_node(node):
    
    if node in graph:
        print("node is already in graph")
    
    else:
        graph[node] = []


add_node("A")
add_node("B")
add_node("C")
add_node("D")
print("Before Adding  Add_Edge")
print(graph)

#======== 4- Function to add an edge using adjadency list representation. ==========


def add_edge(v1,v2,cost):
    if v1 not in graph:
        print(f"{v1} is Not present")
    elif v2 not in graph:
        print(f"{v2} is Not present")
    else:
        list1 = [v2,cost]
        list2 = [v1,cost]
        graph[v1].append(list1)
        graph[v2].append(list2)

print("After adding Add_Edge")

add_edge("A","C",2)
add_edge("A","B",5)
add_edge("D","B",5)
add_edge("D","A",6)
print(graph)


#======== Delete Node Function ======

# here we make function for delete function for weighted and undirected graph.

def deletion(node):
    if node not in graph:
        print(f"{node} vertex is node present in this graph ")
    else:
        del graph[node]
        for key in graph:
            for j in graph[key]:
                if node == j[0]:
                    graph[key].remove(j)

            
# deletion("B")
print(graph)


# ========= Delete edge function ===========

# this is for weighted undirected graph similarly we can do for other graph

def delete_edge(v1,v2):

    if v1 not in graph:
        print(f"{v1} is not present")

    if v2 not in graph:
        print(f"{v2} is not present")

    else:
        for k in graph[v2]: # this is for let suppose both vertex are present but there is no edge between them 
                            # so it give error to here we check weather they present or not in each others value part.
            if k[0] == v1:
                #graph[v1].remove(v2) this is for unweighted graph
                for i in graph[v1]:
                    if i[0] == v2:
                        graph[v1].remove(i) 
                #graph[v2].remove(v1) this is for unweighted graph
                for j in graph[v2]:
                    if j[0] == v1:
                        graph[v2].remove(j)


delete_edge("C","D")
print(graph)