#============= Graph With Multiple Edges ============

'''
If there is multiple edges between two nodes we did not store 1 for show edge between two node
we store that number which show how many nodes are present between 2 nodes.

Effect In functions: In adjacency matrix

add_node(): No effect just add new nodes
add_edge(): Start a counter and when we add edges between same node increment the count.

delete_node(): No effect just delete node
delete_edge(): Decrement the counter.

'''
