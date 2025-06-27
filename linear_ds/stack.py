#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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
"""


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
