# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:09:17 2020

@author: Om Patel
"""
from card import Card

class BinaryTree:
    def __init__(self, c, left_parent = None, right_parent = None):
        self.card = c
        self.parent = None
        self.setRightTree(right_bt)
        self.setLeftTree(left_bt)
        
    def setLeftTree(self, lbt):
        self.left_bt = lbt
        if lbt != None: lbt.parent = self
        
    def setRightTree(self, rbt):
        self.right_bt = rbt
        if rbt != None: rbt.parent = self
    
    def canRemove(self):
        if self.right_bt == None and self.left_bt == None: return True
        return False
    
    