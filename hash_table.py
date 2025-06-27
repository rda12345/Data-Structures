#!/usr/bin/env python3 
# -*- coding: utf-8 -*-
"""
hash_table.py contains an implementation of a simple hash table.
The hash table stores data in pairs of (key,data)
The hash function h(k) gives a new index to store the data linked with k.

Collisions are resolved by the two following methods:
    1. Chaining
    2. Open addressing: linear/quadratic propbing and double hashing


Good for: 
    - constant time lookup and insertion
    - cryptography
    - indexing data

"""

## Chaining
class Pair(object):
    def __init__(self,key,data):
        ''' Each data has an associated key, the pointer is used as a part of the hash table'''
        self.key = key
        self.data = data
        self.pointer = None
        


class HashTable():
    
    def __init__(self,n,hash_function):
        '''Initializes a hash table with n buckets. Maps elements to the buckets
            employing the hash_function.'''
        self.n = n
        self.hash_function = hash_function
        self.table = [None]*self.n
        
    def insert_chaining(self,pair):
        '''Inserts by chaining'''
        index = self.hash_function(pair.key)
        # If the bucket is empty insert the pair into the bucket
        if self.table[index] == None:
           self.table[index] == pair 
        # Otherwise insert the pair after the last pair in the bucket
        else: 
             temp = self.table[index]
             while temp.pointer != None:
                 prev_pair = temp
                 temp = temp.pointer
             prev_pair.pointer = pair    
             
    def delete_chaining(self,pair):
        '''Delete method for when collisions are resolved by chaining'''
        index = self.hash_function(pair.key)
        # If the bucket includes the pair delete it from the bucket
        if self.table[index] == pair:
           self.table[index] == None 
        # Otherwise follow the pointers until reaching pair and remove the last pointer
        else: 
             temp = self.table[index]
             while temp.pointer != pair:
                 prev_pair = temp
                 temp = temp.pointer
             prev_pair.pointer = None 
    
    def insert_open_address(self,pair):
        
    
    def delete_open_address(self,pair):
        
    
    

