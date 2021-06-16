#============= Type Of Graphs =========

'''
Based on direction of the edges  we have two type in Graph:

1- Directed Graph : A graph in which all the edges are uni-directional

2- Undirected Graph: A graph in which all the edges are bi-directional

Based on weight we have two type of Graph:

1-Weighted Graph : A graph in which each edge is assigned with some weight/cost/value.

2-Unweighted Graph: A graph where there is no value or weight associated with the edge.

Based on graph contain cycle or not we have two type of graph:

1-Cyclic Graph : if contain cycle then cyclic graph
   
2-Acyclic Graph : if not contain cycle then Acyclic Graph.
     # Tree is a acyclic graph.

'''


# =========== Terminologies of Graph ============

'''
-->node/vertex
--> Adjacent Nodes / Neighbour Nodes :
            Node X is adjacent node Y if there is an edge from node X to node Y.

--> Path : Sequence of vertices in which each pair of successive nodes is connected by an edge.
        Length of path : Number of edges present in that path.
        length of path never be 0  it should be greater or equal to 1.

    Type of Path :
    Simple Path : A Path is simple if all of its vertices/nodes are distinct

    Closed Path: A Path is closed if the first and last node of that path is same. 
                # here vertices can be repeat 

    Cycle : Cycle is path in which first and last node need to be same and also all the
            other nodes need to be distinct.
        
--> Connected Graph - In undirected , A graph is said to be connected if there is a path from any node to any other node.

--> Strongly Connected Graph : In directed graph if there is a path from any node to any other node.
                # here we have to take care of direction of graph it is such a way that we can reach 
                from any node to any node.
    
--> Weakily connected Graph :In a directed graph, here we see graph as undirected graph and if we find it is connected graph
                    then we can say it is weakily connected graph.

--> Degree of a Node : In a undirected graph number of edges connected to the node is the degree 
                        of the node.

--> Degree In Directed Graph:

                Indegree of a node = Number of edeges coming to that node.
                Outdegree of a node = Number of edges outside from that node

--> Complete Graph : A graph is complete if there is an edges between every pair of graph.
                # here each node connected such that it  connect with all node in that graph .


'''