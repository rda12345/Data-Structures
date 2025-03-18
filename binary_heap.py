#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary heap

A heap DS is a complete binary tree that satisfies the heap property:
    Max heap: any given node is always bigger than its childs node/s. 
    
    Operations:
        Heapify:
            
            1. Create a complete binary tree from the input array (0 is the route,
                1,2 its children and so on).
            2. Start from the first index of non-leaf node whose index is given by n/2 - 1.
            3. Set the current element i as largest.
            4. Set its left child index to 2*i+1 and its right child index to 2*i+2
            5. If leftChild > currentElement set largest = leftChildIndex, if 
                rightChild > largest set largest = rightChild.
            6. Swap largest and current Element
            7. Repat 3-7 until the subtrees are also heapified.
            
        Delete: Recieves and index of the deleted item, swaps it with the last
                leaf and max-heapifies the list.
        
        Insert: Inserts and item and returns a heapified list. Inserts the item
                in the last leaf and heapifies the tree.
            
        Peek/Find min/max: 
    Time complexity:
        Heapify:  Builds the heap in O(n)
        Insert: 
        Delete:
            
    Good for: 
        1. Heap sort
        2. Dijstra's algorithm
        3. Priority queue
"""

class Heap(object):
    
    def __init__(self,L):
        '''L is a python list'''
        self.L = L
        self.n = len(L)
    
    def __str__(self):
        return str(self.L)
        
    def max_heapify(self,n,i):
        left = 2*i + 1     # left child index
        right = 2*i + 2     # right  child indes
        largest = i
        
        if left < self.n and self.L[left] > self.L[largest]:
            largest = left
            
        if right < self.n and self.L[right] > self.L[largest]:
            largest = right
        
        if largest != i:
            self.L[largest], self.L[i] = self.L[i], self.L[largest]
            self.max_heapify(n,largest)

    def max_heapify_list(self):
        '''Max heapifies the entire list'''        
        for i in range(self.n//2-1,-1,-1):
            self.max_heapify(self.n,i)
            
    def delete_node(self,index):
        '''Deletes the element L[index]. Algorithm swaps L[index] with the last
            leaf and heapifies the list. 
        '''
        if index < self.n:
            self.L[index], self.L[self.n-1] = self.L[self.n-1], self.L[index]
            self.L.pop()
            self.n -= 1
            self.max_heapify_list()
        else:
            print('Index out of range')
            
    def peek(self):
        '''Returns the root node (the maximum for a max heap and the minimum
            for a min-heap).
        '''
        return self.L[0] 
    
    
    def extract_max(self):
        '''Extracts the maximum item, which is located at the root of the tree,
            assuming the list is max-heapified.
        '''
        temp = self.L[0]
        self.delete_node(0)
        return temp
    
    def insert(self,item):
        '''Inserts the item in the last leaf and heapifies the tree.'''
        self.L.append(item)
        self.n += 1
        self.max_heapify_list()
        
        
        
            
# Max heapify the list L        
# L = [7,7,12,2,8,9,10]
# h = Heap(L)
# h.max_heapify_list() 
# print(h)
# h.insert(6)
# h.insert(20)
# print(h)
# print(h.peek())
# h.extract_max()
# print(h)
# h.delete_node(2)
# print(h)
 

    
        