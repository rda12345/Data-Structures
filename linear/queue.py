#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Queue: 
    First in first out principle. There are two pointers, front and rear, the 
    front tracks the first element of the queue and rear is the last element.
    Initially, both front and rear are initialized to -1. When adding items 
    to the queue modify front and rear so front = 0 and rear = # of items - 1.
    
    Operations:
        1. enqueue - add an element to the begining of the queue
        2. dequeue - remove an element at the end of the queue
        3. isEmpty - check if the stack is empty
        4. isFull - check if the stack is full
        5. peek - get the value of the front of the queue without removing it

    Time complexity:
        All operations take O(1) (note: it is important not to use pop(1) to
                                  dequeue as it takes O(n))
    Good for: 
        - CPU/disk scheduling
        - Synchronize processes
        - Call center, plane arrival scheduling
"""



class Queue(object):
    
    def __init__(self,size):
        ''' size: the maxium number of items added to the queue.'''
        self.size = size
        self.queue = [None]*size
        self.front = -1
        self.rear = -1
    
    def __str__(self):
        return str(self.queue[self.front:self.rear+1])
    
    # Insert an item to the queue
    def enqueue(self,item):
        
        if self.rear == self.size - 1:
            print('The queue is full\n')
        elif self.front == -1 :
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = item

        else: 
            self.rear += 1
            self.queue[self.rear] = item
            
        
    # Remove an item from the queue
    def dequeue(self):
        
        if self.front == -1 :
            print('The queue is empty\n')
        elif self.front == self.rear:
            item = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return item
        else:
            self.front += 1
            return self.queue[self.front - 1]
        
    def is_empty(self):
            return self.front == -1
            
    def is_full(self):
            return self.rear == self.size -1
        
    def peek(self):
            if self.front > -1:
                return self.queue[self.front]
        
## Check Queue
# obj = Queue(5)
# obj.enqueue(1)
# obj.enqueue(2)
# obj.enqueue(3)
# obj.enqueue(4)
# obj.enqueue(5)
# print(obj)
# obj.dequeue()
# print(obj)
# print(obj.peek())  
# print(obj.is_empty())
# print(obj.is_full())

