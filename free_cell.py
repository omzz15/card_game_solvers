# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:47:58 2020

@author: q774283
"""

from game import CardGame

class FreeCell(CardGame):
    
    def __init__(self):
        super().__init__(4, 4, 8)
        self.card_receive_flags = [(False, True, True), (False, False, True), (True, True, True)]
