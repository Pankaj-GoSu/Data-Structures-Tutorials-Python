#======= Binary Heap Operations =============

'''
1- Heapify: it is a process to rearrage the elements of the heap in order to maintain 
            the heap property.
            -> make sure that every node of tree follows heap property.
            -> used to create binary heap from a complete binary tree.
    to make a complete binary tree to heap binary tree this process is done by Heapify operation.

There are Two type in this heapfy operation:
Heapify up : follows bottom up approach.
Heapify down : follows top down approach

2- Insertion: inserting a new node to binary heap by maintaining its properties.

step1- add the new node to first open spot available in the lower level.
step2- Heapify the new node
 
3- Deletion: Removing the node from binary heap by maintaing its properties. 

step1- swap the node you want to delete with the last node. so that complete tree is maintained
step2- delete the last node.
step3- heapify the last node which is now places in the deleted node position

4- Extract min/max key: In this operation we print the root node value and we delete root node.

5- Get min/max: Here we need to print root node key.
                       

'''
