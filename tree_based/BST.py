#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Binary search tree (BST)
The data supports search, insert and delete, find min/max, next larger/smaller
in O(log(h)) running time, where h is the hieght of the tree.
The hieght of the tree is the maximum number of edges between the leaf and
                                   the root.
"""

class BSTNode(object):
    """A node in a BST tree"""
    def __init__(self,k):
        """ Creates a node.
            
            Args:
                parent: BSTNode, the node's parent
                key: float, the node's key
            
            Parms:
                left: BSTNode, the left child node.
                right: BSTNode, the right child node.
        """
        self.key = k
        self.left = None
        self.right = None
        self.parent = None 
        
    def __str__(self):
        return str(self.key)
    
        
    
    def find(self,k):
        """Finds and returns the node with key k from the subtree rooted at this node."""
        if self.key == k:
            return self
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)
    
    def find_min(self):
        """Finds and returns the minimum element of the BST rooted at the node"""
        # Base case:
        if self.left is None:
            return self
        else: 
            return self.left.find_min()
    
    def find_max(self):
        """Finds and returns the minimum element of the BST rooted at the node"""
        # Base case:
        if self.right == None:
            return self
        else: 
            return self.right.find_max()
    
    def insert(self,node):
        """Inserts a node into the subtree rooted at this node.
            (it is assumed each key is distinct)
        
        Args: 
            node: BSTNode, the node to be inserted
        
        Returns:
            node: the inserted node
        """
        if node.key < self.key:
            if self.left is not None:
                return self.left.insert(node)
            node.parent = self
            self.left = node
            return node

        elif node.key > self.key:          
            if self.right is not None:
                return self.right.insert(node)
            node.parent = self
            self.right = node
            return node
        return self
            
    def next_larger(self):
        """Finds the node with the next larger key"""
        # Base case: the right child of the node is None
        if self.right == None:
            if self.parent == None or self == self.parent.right:
                raise NameError('This is the largest key')
            else:
                return self.parent
        else: 
            return self.right.find_min()
        
    def next_smaller(self):
        """Finds the node with the next smaller key"""
        # Base case: the right childe of the node is None
        if self.left == None:
            if self.parent == None or self == self.parent.left:
                raise NameError('This is the smallest key')
            else:
                return self.parent
        else: 
            return self.left.find_max()    
    
        
                
    #def delete(self):
      #"""
      # Deletes this node from the BST. Applies a simiple method which 
      # uses a key replacement for the case
      # where the deleted nodes children aren't None. 
      #"""
     # if self.left is None or self.right is None:
      #  if self is self.parent.left:
      #    self.parent.left = self.left or self.right
      #    if self.parent.left is not None:
      #      self.parent.left.parent = self.parent
      #  else:
      #    self.parent.right = self.left or self.right
      #    if self.parent.right is not None:
      #      self.parent.right.parent = self.parent
      #  return self
      #else:
      #  s = self.next_larger()
      #  # NOTE: deleting before swapping the keys so the BST RI is never violated.
      #  deleted_node = s.delete()
      #  self.key, s.key = s.key, self.key
      #  return deleted_node
    
    
    def delete(self):
        """
            Deletes this node from the BST.
        """
        y = self.next_larger()
        #cases 1 and 2: one of the self's children is None or both
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
            else:
                self.parent.right = self.right or self.left
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
        #case 3: self.right.left == None (meaning the next_larger(self) = self.right)
        elif  y == self.right:
            y.left = self.left
            self.left.parent = y
            y.parent = self.parent
            if self == self.parent.left:
                self.parent.left = y
            else:
                self.parent.right = y
        #case 4: self.right.left != None
        else:        
            y.parent.left = y.right
            y.right.parent = y.parent
            
            y.right  = self.right
            self.right.parent = y
            
            y.left = self.left
            self.left.parent = y
            y.parent = self.parent
            if self == self.parent.left:
                self.parent.left = y
            else:
                self.parent.right = y   
        return self    
            
                 
        
    
        
    def check_ri(self):
        """
        Checks the representation invariant (RI) of the AVL tree. 
        Namely, that the tree is a binary search tree:
        node.left.key < node.key && node.right.key > node.key for every node
        in the tree.
        
        """
        # Base case: if the node is a leaf it satisfies the representation invariant
        if self.left == None and self.right == None:
            return True
        elif self.left == None and self.right.key > self.key:
            return self.right.check_ri()
        elif self.right == None and self.left.key < self.key:
            return self.left.check_ri()
        elif self.right.key > self.key and self.left.key < self.key:
            return self.left.check_ri() and self.right.check_ri()
        else: 
            return False

class BST(object):
    """Creates a binary search tree"""
    
    def __init__(self,node_class = BSTNode):
        """Creates and emptly BST"""        
        self.node_class = node_class
        self.root = None
        
    def min(self):
        if self.root is None:
            return None
        else:
            return self.root.find_min()
            
     
    def insert(self, key):
        node = self.node_class(key)
        if self.root is None:
           self.root = node
           return node
        else:
            return self.root.insert(node)
            
            
    def find(self,key):
        return self.root and self.root.find(key)
   
    
    def check_ri(self):
        return self.root and self.root.check_ri()
       
    def delete(self,key):
        node = self.find(key)
        if node:
            if node == self.root:
                pseudo_root = self.node_class(None)
                pseudo_root.left = self.root 
                self.root.parent = pseudo_root
                deleted_node = node.delete()
                self.root = pseudo_root.left
                return deleted_node
            else:
                return node.delete()
        else:
            return None
        
    def successor(self,key):
        node = self.find(key)
        return node and node.next_larger()        
  

l = []         
def inorder(node):
    if node != None:     
       #print(node.key)
       inorder(node.left)
       l.append(node.key)
       inorder(node.right)
       
       
"""     
if __name__ == '__main__':
    ### BST check
    tree = BST()
    tree.insert(10)
    tree.insert(11)
    tree.insert(18)
    tree.insert(6)
    tree.insert(2)
    
    ## insert check
    print(tree.check_ri())    
    
    ## find check
    print(tree.find(11))
    print(tree.find(1))
    
    ## min check
    print(tree.min())
    
    ## successor check
    print(tree.successor(6))
    print(tree.successor(16))
 
    ## delete check
    tree.delete(10)
    tree.delete(11)
    tree.delete(0)
    l = []    
    inorder(tree.root)
    print(f'tree transversal: {l}')
    print(f'RI check: {tree.check_ri()}')    
        
    ### BSTNode check                    
    root = BSTNode(10)
    root.insert(BSTNode(9))
    root.insert(BSTNode(11))
    root.insert(BSTNode(13))
    root.insert(BSTNode(6))
    root.insert(BSTNode(12))
    

    ## insert check
    
    l = []    
    inorder(root)
    print(f'tree transversal: {l}')
    print(f'RI check: {root.check_ri()}')
    
    ## delete check
   
    print(f'deleted node: {root.left.key}')
    root.left.delete()
    print(f'deleted node: {root.left.key}')
    root.left.delete()
    l = []
    inorder(root)
    print(f'tree transversal: {l}')
    print(f'RI check: {root.check_ri()}')
    
    root.insert(BSTNode(6))
    root.insert(BSTNode(9))

    
    ## find check
    #print(root.find(6))
    #print(root.find(55))
    # find_min check
    print(f'minimum: {root.find_min()}')
    print(f'maximum: {root.find_max()}')
    
    
    # next_greatest check
    print(f'root.key = {root}')
    print(f'next larger: {root.next_larger()}')
    
    # next_smallest check
    print(f'next smaller: {root.next_smaller()}')

"""
    
