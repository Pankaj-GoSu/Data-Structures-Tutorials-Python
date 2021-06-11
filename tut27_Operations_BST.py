#=========== Operations of Binary Search Tree ==============

'''
Operations:

1- Search: searching a node in BST. begin from root node.
--> BST -> Empty -> Given Value not present.
--> root == given value -> given value is present
        if not then it check given value is less or greater then node value.
        if given value < root node --> It search into left sub tree.
        if given value > root node --> It search into right sub tree.

Then after that repeat above process. until you get your given value or search is completed.

2- Insertion: Insertion operation is for insert a new node with given value at correct postion in BST

step1 - BST -> Empty : insert new node.
        
        root == new_node (it means we add duplicate value and do a/c to your application how you treat duplicate.)

        root < new_node : go into right side and insert new node in right side of root node.
        root > new_node : go into left side and insert new node in left side of root node.

Then after that repeat above process . until you insert that new node to your BST.

3- Deletion : It delete the given node if it is present in BST.

step1 - BST -> Empty :can't delete print message.

    if not empty then search for that given node value which you want to delete.
            if not present in BST we print a message .
            if present in BST then we have to delete that node and take care all rules 
            of BST.
    
    Here we face 3 type of condition:
    
    User want to delete a node and that node may be:
    
    case:1- node with 0 child node -> find that node and delete it
    case:2- node with 1 child node -> find that node and replace that node with its child. 
            and replace as its postion if it is in right that replace in right vice versa.
    case:3- node with 2 child node -> find that node and replace that node with greatest 
            value in left side or smallest value in right side.

4- Traversing A BST : Traversing a BST is a process of visting each node in tree exactly one time.
                      
                      Tree is a non linear data structure like queue or stack we can not traverse it sequencely.


        Travesal Algorithems :

        1- Pre-order Traversal:(for remebering --> root visit first so pre-order) 

                To Traverse a non-empty BST in pre-order , the following operations are performed
                recursively at each node.
                1- visit the root node
                2- Traversing the left sub-tree and finally
                3- traversing the right sub-tree

                example : 30(root node) , 10(left node ) , 50(right node)

        2- In-Order Traversal:(for remebering --> root visit in middle so in-order)

                To Traverse a non-empty BST in in-order , the following operations are performed
                recursively at each node.
                1- Traversing the left sub-tree.
                2- visit the root node and finally
                3- traversing the right sub-tree

                example : 10(left node), 30(root node), 50(right node)
        # here we get values in accending order.

        3- Post-Order Traversal(for remebering --> root visit at last means post-otder so it is post-order)
                
                To Traverse a non-empty BST in in-order , the following operations are performed
                recursively at each node.
                1- Treversing the left sub-tree
                2- Trversing the right sub-tree and finally
                3- visit the root node

                example: 10(left node), 50(right node), 30(root node)

        4- Level-Order Traversal: In this algorithem all the node are accesed in a 
                                  level before going to another level. Means we visting the nodes level wise.

                It start from level zero.


        
''' 