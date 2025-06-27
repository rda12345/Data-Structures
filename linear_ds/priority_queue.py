#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Priority Queue:
    Values are removed on the basis of priority.
    Priority queue can be implemented using an array, a linked list,
    a heap data structure, or a binary search tree.
    Linked list: peek O(1), insert O(n), delete O(1)
    Binary heap: peek O(1), insert O(lg(n)), delete O(lg(n))
    Binary search tree: peek O(1), insert O(lg(n)), delete O(lg(n))
    
    The implementation utilizes the Binary heap ADS (abstract data structure).
    
    Operations:
        1. insert
        2. delete
        3. peek
        4. isEmpty
        5. isFull
    
    Time complexity: The complexity is identical to the heap.
                    An insertion costs at most O(lg(n)) (requires heapifing the list after insertion)
                    therefore the initial building of the heap takes O(n*log(n))
                    1. insertion O(lg(n))
                    2. delete O(lg(n))
                    3. extract max O(lg(n)) (requires heapifing the list after insertion)
                    4. peek O(1)

    Good for:
        - Dijkstra's algorithm
        - Load balancing and interrupt hanling of an operating system
        - Data compression in the Huffman code      
"""


## Priority queue - Implementation using the heap data structure
from binary_heap import Heap 
        
L = [7,7,12,2,8,9,10]
p = Heap(L)


class Deque(object):
    
    def __init__(self,size):
        ''' size: the maximum number of items in the queue.'''
        self.size = size
        self.queue = [None]*self.size
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        return str(self.queue)
    
    # Insert an item to the front of the deque
    def insert_front(self,item):
        if self.is_full():
            print('The queue is full\n')
        elif self.front == -1 :
            self.front = 0
            self.queue[self.front] = item
            self.rear = 0
        else:
            self.front = (self.size - 1 + self.front)%self.size
            self.queue[self.front] = item
            
    # Insert an item to the front of the deque
    def insert_rear(self,item):
        
        if self.is_full():
            print('The queue is full\n')
        elif self.rear == -1 :
            self.queue[0] = item
            self.front = 0
            self.rear =  0
        else:
            self.rear = (self.size + 1 + self.rear)%self.size
            self.queue[self.rear] = item
            
    # Remove an item from the front of the deque
    def delete_front(self):
        if self.is_empty():
            print('The queue is empty\n')
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front = (self.size + 1 + self.front)%self.size
            return item
        
        
    def delete_rear(self):
        
        if self.is_empty():
            print('The queue is empty\n')
        elif self.front == self.rear:
            item = self.queue[self.rear]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.queue[self.rear]
            self.rear = (self.size - 1 + self.rear)%self.size
            return item
        
    def is_empty(self):
            return self.front == -1
            
    def is_full(self):
            condition1 = self.rear + 1 == self.front
            condition2 = self.front == 0 and self.rear == self.size -1
            return condition1 or condition2
            

## Check Deque
# d = Deque(5)

# print(d.is_empty())
# print(d)
# d.insert_rear(8)
# print(d)
# d.insert_rear(2)
# print(d)
# d.insert_front(5)
# print(d)
# d.insert_front(10)
# print(d)
# print(d.size)
# print(d.is_empty())
# d.insert_front(1)
# print(d)
# print('f',d.front)
# print('r',d.rear)
# print(d.is_full())
# d.delete_rear()
# print(d)
# print(d.delete_front())
# print('f',d.front)
# print('r',d.rear)
# d.insert_front(55)
# d.insert_rear(30)
# print(d)

