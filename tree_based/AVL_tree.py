#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AVL tree

A data structure which maintains a balanced binary search tree.
Search, insert, delete, find min/max, find smallest/largest are O(log(N)).
And building the AVL takes O(N*log(N)) running time.
"""
from BST import BSTNode, BST

       
       
                
class AVLNode(BSTNode):
    
    def __init__(self,key):
        """Create as a node which will be inserted into the AVL tree"""
        BSTNode.__init__(self,key)  
        self.height = 0
        
    def update_subtree_info(self):
        """Updates the nodes info"""
        self.height = self.updated_height()
    
    def updated_height(self):
        """Updates the node's height"""
        return 1 + max((self.left and self.left.height) or -1,
                       (self.right and self.right.height) or -1)
        
        
    def check_ri(self):
        """Checks the representation invariant of the AVL node"""
        if self.height != self.updated_height():
            raise NameError('RI is violated by wrong node height')
        if abs(height(self.left)-height(self.right)) >= 2:
            raise NameError('RI violated by unbalanced node height')
        return BSTNode.check_ri(self)

   

class AVL(BST):
    
    
    def __init__(self, node_class = AVLNode):
        """Initiates an AVL tree"""
        BST.__init__(self,node_class)
        
        
        
    def insert(self,key):
        """Inserts a node to the AVL tree and rebalances the tree"""
        inserted_node = BST.insert(self, key)
        self.rebalance(inserted_node)
        return inserted_node
        
        
    def delete(self,key):
        """Deletes a node with node.key = key from the tree"""
        deleted_node = BST.delete(self, key)
        if deleted_node:
            self.rebalance(deleted_node.parent)
        return deleted_node
        
    def rebalance(self,node):
        """Rebalances the tree by right and left rotations. 
        """
        #We begin the procedure from the leafs to the root.    
        while node is not None:
            node.update_subtree_info()

            #There are two cases 
            #case 1: the left child of node x is heavier than the right child.
            #       inserting into the left child may violate the AVL tree
            if height(node.left) >= 2 + height(node.right):
                if height(node.left) >= height(node.right):
                    self.right_rotate(node)
                else:
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            
            #case 2: analogous to case 1 but with left -> right
            if height(node.right) >= 2 + height(node.left):
                if height(node.right) >= height(node.left):
                    
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)   
            #updating the node (going up the tree towards the root)
            node = node.parent
        
         
           
    def left_rotate(self,y):
        """Performs a left rotation w.r.t node y"""
        x = y.right
        x.parent = y.parent
        if y.parent == None:
            self.root = x
        else:
            if y.parent.left == y:
                y.parent.left = x
            else:
                y.parent.right = x
        y.parent = x
        y.right = x.left
        if y.right is not None:
           y.right.parent = y
        x.left = y
        #update the information
        x.update_subtree_info()
        y.update_subtree_info()
        
    def right_rotate(self,x):
        """Performs a right rotation w.r.t node y"""
        y = x.left
        y.parent = x.parent
        if y.parent == None:
            self.root = y
        else:
            if x.parent.left == x:
                x.parent.left = y
            else:
                x.parent.right = y
        x.parent = y
        x.left = y.right
        if x.left is not None:
           x.left.parent = x
        y.right = x
        #update the information
        x.update_subtree_info()
        y.update_subtree_info()
        
        
def height(node):
    """Returns the height of the the node"""
    if node is None:
        return -1
    else: 
        return node.height
    
    
    
l = []    
def inorder(node):
    if node != None:     
       inorder(node.left)
       l.append(node.key)
       inorder(node.right)

    
"""    
if __name__ == '__main__':
    
    ### AVL check
    tree = AVL()
    keys = [10,11,18,6,2]
    for key in keys:
        tree.insert(key)

    ## insert check
    l = []    
    inorder(tree.root)
    print(f'tree transversal: {l}')
    for key in keys:
        node = tree.find(key)
        node.check_ri()
    
 
    ## delete check
    tree.delete(10)
    tree.delete(11)
    tree.delete(0)
    l = []    
    inorder(tree.root)
    print(f'tree transversal: {l}')
    for key in [2,6,18]:
        node = tree.find(key)
        node.check_ri()
    
    print(f'RI check: {tree.check_ri()}')
"""
    



    
    
    
    




