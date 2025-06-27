#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Circular Queue:
    The cirular queue saves the inefficiency in memory of the regular queue.
    Similar operations and time-complexity as the regular queue.
    
    Good for: 
        - CPU scheduling
        - Memory management
        - Traffic management
"""

class CircularQueue(object):
    
    def __init__(self,size):
        ''' size: the maximum number of items in the queue.'''
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        if self.rear <= self.front:
            return str(self.queue[self.front:self.size]+self.queue[:(self.rear+1)])
        else:
            return str(self.queue[self.front:self.rear+1])
    
    # Insert an item to the queue
    def enqueue(self,item):
        
        if self.is_full():
            print('The queue is full\n')
        elif self.front == -1 :
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item
        else: 
            self.rear += 1
            if self.rear == self.size:
                self.rear = self.rear % self.size
            self.queue[self.rear] = item

            
        
    # Remove an item from the queue
    def dequeue(self):
        
        if self.is_empty():
            print('The queue is empty\n')
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            item = self.queue[self.front]
            self.front += 1
            if self.front == self.size:
                self.front = self.front % self.size
            return item
        
    def is_empty(self):
            return self.front == -1
            
    def is_full(self):
            condition1 = self.rear + 1 == self.front
            condition2 = self.front == 0 and self.rear == self.size -1
            return condition1 or condition2
            
    def peek(self):
            if self.front > -1:
                return self.queue[self.front]    
        
        
        
## Check Circular Queue
# obj = CircularQueue(5)
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.enqueue(5)
# print(obj)
# print(obj.is_full())
# obj.dequeue()
# obj.dequeue()
# print(obj)
# obj.enqueue(6)
# obj.enqueue(7)
# print('check', obj)
# print(obj.peek())  
# print(obj.is_empty())
# print(obj.is_full())        
