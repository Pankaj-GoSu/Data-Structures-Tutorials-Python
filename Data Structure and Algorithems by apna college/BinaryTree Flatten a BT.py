# ========= Flatten a Binary Tree ===========

'''
Problem statement: 
Given a binary tree, flatten it into linked list inplace.
After flattning ,left of each node should point to NULL and
right should contain next node in preorder sequence.
Example:
   1               1 # so here left child is None and it is in preorder
  / \               \
 2   3               2
    /                 \
   4                    3
                         \
                          4   

'''
from typing import NewType


class Node1:

    def __init__(self,data):
        self.data = data
        self.prv = None
        self.next = None


class Doubly_linkedlist:

    def __init__(self):
        self.head = None

    def insert(self,data):
        new_node = Node1(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            new_node.prv = None

    def print_dll(self):
        if self.head is None:
            print("Doubly linked list is empty")
        else:
            n = self.head
            while n != None:
                print(n.data)
                n = n.next
class Node:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def preorder(node):
    list_preorder.append(node.data)
    if node.lchild:
        preorder(node.lchild)
    if node.rchild:
        preorder(node.rchild)

list_preorder = []
node =Node(15)
node.lchild = Node(12)
node.rchild = Node(8)
node.lchild.rchild = Node(19)
node.lchild.lchild = Node(13)
node.rchild.lchild = Node(14)
node.rchild.rchild = Node(18)

DLL = Doubly_linkedlist()
preorder(node)
print(list_preorder)

for i in range(len(list_preorder)-1,-1,-1):
    DLL.insert(list_preorder[i])

DLL.print_dll()
print(DLL.head.next.data)
print(DLL.head.next.prv) # so here we see left child of Binary tree is None as asked in our question.