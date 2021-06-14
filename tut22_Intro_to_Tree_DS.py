#============= Introduction To Tree Data Structure ====================

# Tree is non linear data structure which repersent relationship between the different Nodes.

# Tree DS is collection of entities called Nodes.
# Nodes are connected by edges.
# each Node of tree contain data and it may or may not have childerens.

'''
# Tree related Terms:
1- Nodes : The indivisual elements of tree is called nodes, every node contains data and links to other node.
2- Root Node : Top most Node of tree is called Root Node, root node is origin of tree data structure.
# In any tree there is must be 1 root node,we never have multiple root nodes in tree.
3- Edge/Link : connection between two nodes
4- Parent Node/Parent: Nodes which has child or childeren. 
5: Child Node / Child : the node which have connection with parent node is called child node.
#Nodes Contain Any number of childerens.
# In a tree all the nodes except root Node are the child Nodes.
6: Siblings : Nodes which belong to same parent are called as siblings.
7- Leaf Node / Leaf/External Node/ Terminal Node: Node which does not have a child is called as leaf node or is also knowen as external node.

8- Internal Node : the node which have at least one child is called internal node.
9- Path : The Sequence of node and edges from one node to another is path between 2 Nodes. 

'''


#============ Characteistics of Tree ===============

'''
1- Root Node : top most node(A tree can contain only one root node)
root Node is used to travesed each node of tree. 
tree originate from root node.

2- In a tree if we have N nodes then no. of edgs / link is N-1.

3- Every child will have only one parent but parent can have multiple child.

4- Tree actually contain trees within them that means trees are Recursive Data Structure.
tree contain sub trees.
 

'''

# ======== Few More Terms In Tree =================

'''
Degree: you can found out degree of tree or degree of a node.

1- Degree of a Node : Total no. of childeren of Node is degree of that node.
2- Degree of a Tree : It is the  highest Degree of Node among the all nodes.
for calculating Degree of a tree first we have to calculate degree of each node and then max value is degree of tree. 
# Degree of leaf node is 0.

Level: In a tree each step from top to bottom is called as level of tree.the level count start from 0.

Root Node at level 0.
So here we can find level of tree.

Height: Hieght we see from ground so it start from leaf nodes.
1- Height of a node: total number of edges which lies on the longest path from any leaf node to a perticular node.

2- Height of a tree: total number of edges-> height of the root node.(it is calculated by any leaf node to root node by taking longest path)

Height of leaf node is 0

Depth : Depth we see from top so it start from root node.

1- Depth of node : total number of edges from root node to that perticular node.
first find the path from root node to that node after that count number of edegs.
It means depth of Root Node ia always 0.

2- Depth of tree : total number of edges from root node to leaf node by taking longest path.


'''