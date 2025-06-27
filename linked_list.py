#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linked list:
    A series of connected nodes, each node stores the data and an address of the next node.
    The address of the first node is the 'head' and the the last node points to a NULL.
    You create a linked list by: introducing the nodes, allocating memory for the associated data,
    connect the nodes.
    The power of a linked list comes from the ability to break the chian and rejoin it.
    
    Operations:
        1. search
        2. insertion
        3. deletion
        4. transversal - access each element of the linked list
    
    Good for:
        - Dynamic memory allocation
        - Implemented in stack and queue
        - In undo functionality of softwares
        - Hash tables, Graphs
        
    Time complexity:
        1. search is both worst case and average case O(n) 
        2. insertion is both worst case and average case O(1)
        3. deletion is both worst case and average case O(1)
"""

class Node(object):
    
    def __init__(self,item):
        '''Creates a node, includes an item and a pointer (next) to the next node in the linked list.'''
        self.head = item
        self.next = None
    
    def __str__(self):
        return str(self.head)
    
class LinkedList(object):
    
    def __init__(self):
        '''Create a linked list of nodes.'''
        self.head = None
    
    def transversal(self):
        '''Prints a linked list'''
        temp = self.head
        string = ''
        print('Linked list elements:')
        while temp != None:
            string = string+ str(temp)+'-->'
            temp = temp.next
        print(string[:-3])
    
    def insert(self,node,node_before = None):
        '''Inserts a node 'node' ofter the 'before_node'.'''
        if  node_before == None:
            node.next = self.head
            self.head = node
        else:
            node.next = node_before.next
            node_before.next = node
    
    def delete(self,node):
        '''Delete node from the linked list'''
        if self.head == node:
            self.head = node.next
        else:
            current_node = self.head
            while current_node != node:
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = node.next
        
    def search(self,node):
        '''Returns True if node is in the linked list and False otherwise.'''
        current_node = self.head
        while current_node != node and current_node != None:
            current_node = current_node.next
            
        if current_node == node:
            return True
        else:
            return False
    
    
        

    
    
## Check linked list
        
# # Creating the nodes
# first = Node(1)
# second = Node(2)
# third = Node(3)

# # Checking the transversal method

# # Pointing the head to the first node
# LL = LinkedList()
# LL.head = first
# # Pointing the first node to the second node.
# LL.head.next = second
# # Pointing the second node to the third node.
# second.next = third
# LL.transversal()

# # Checking the insertion method
# middle = Node('a')
# LL.insert(middle,second)
# LL.transversal()

# middle2 = Node('c')
# LL.insert(middle2)
# LL.transversal()
    
# # Checking the deletion method
# LL.delete(first)
# LL.transversal()
# LL.delete(middle)
# LL.transversal()

# # Checking the search method
# print(LL.search(first))
# print(LL.search(middle2))        
