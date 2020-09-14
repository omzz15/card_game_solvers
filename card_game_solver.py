# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:36:29 2020

@author: q774283
"""

class CardGameSolver:
        
    def __init__(self, 
                 end_func = self.end_function, move_func = self.moves_function):
        self.end_func = end_func
        self.moves_function = move_func
        
    def end_function(self):
        return True

    def moves_function(self):
        return []
    
