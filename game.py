# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:42:53 2020

@author: q774283
"""
from card import Card, CardPlaces, CardList

class CardGame:
    
    def __init__(self, foundation_size = 0, cell_size = 0, working_stack_size = 0):
        self.foundation = [CardList(CardPlaces.FOUNDATION) for i in range(foundation_size)]
        self.cell = [CardList(CardPlaces.CELL) for i in range(cell_size)]
        self.working_stack = [CardList(CardPlaces.WORKING_STACK) for i in range(working_stack_size)]
        self.card_lists = {
                CardPlaces.FOUNDATION.value: self.foundation,
                CardPlaces.CELL.value: self.cell,
                CardPlaces.WORKING_STACK: self.working_stack
                }
        self.card_receive_flags = [(True, True, True), (True, True, True), (True, True, True)]

    def can_move(self, from_card_list, to_card_list):
        return True
        
    def move(self, from_place_idx, to_place_idx):
        pass