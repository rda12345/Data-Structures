#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Linear data structures:
    
    Following the explanations of progamiz.com
    
    1. Stack
    2. Queue
    3. Circular Queue
    4. Priority Queue

Stack: 
    Last in first out (LIFO) principle. There is a single pointer top, initialliy
    set to -1 when you push an item you increment the pointer by one and insert the
    item to the stack.

    Operations: 
            1. push - add an element to the top of the stack
            2. pop - remove an element from the top of the stack
            3. isEmpyt - check if the stack is empty
            4. isFull - check if the stack is full
            5. Peek - get the value at the top of the stack without removing it

    Time complexity:
        All operations above take O(1)

    Good for: 
        - Reverse a word
        - Used by compilers to evaluate arithmetic expressions, by converting 
            the expressions to prefix of posfix form.
        - In browsers to control back forward commands.

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
        
        
Circular Queue:
    The cirular queue saves the inefficiency in memory of the regular queue.
    Similar operations and time-complexity as the regular queue.
    
    Good for: 
        - CPU scheduling
        - Memory management
        - Traffic management
        

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
    
    
Dequeue:
    A double ended queue, where insert and removal can either be performed from
    the front or from the rear. The present implementation utilizes a circular 
    array.  
    
    Operations:
        1. Insert at the front
        2. Insert at the rear
        3. Delete at the front
        4. Delete at the rear
    
    Time complexity:
        Similar to the circular queue
        
        

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
## Stack

class Stack(object):
    
    def __init__(self,size):
        ''' size: the maximum number of elements in the stack'''
        self.size = size
        self.stack = []
    
    def __str__(self):
        return str(self.stack)
        
        
    def is_empty(self):
        return len(self.stack) == 0
        
    def is_full(self):
        return len(self.stack) == self.size
        
    def push(self,item):
        if len(self.stack) < self.size:
            self.stack.append(item)
        else:
            print('Stack is full')
        
        
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            print('Stack is empty')
        
    def peek(self):
        return self.stack[-1]
    

## Stack check 
# a = Stack(3)
# a.pop()
# print(a.is_empty())
# a.push(1)
# a.push(2)
# print(a)
# a.push(3)
# a.push(4)
# a.pop()
# a.pop()
# print(a)
# print(a.peek())


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

## Priority queue - Implementation using the heap data structure
from binary_heap import Heap 
        
## Check Priority queue
L = [7,7,12,2,8,9,10]
p = Heap(L)
# print(p.peek())
# p.delete_node(1)
# print(p)
# p.insert(10)
# print(p)
# p.extract_max()
# print(p)

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

## Linked list

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
    
