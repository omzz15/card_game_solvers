# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:34:54 2020

@author: q774283
"""

from enum import Enum, auto

class CardSuite(Enum):
    HEART   = auto()
    SPADE   = auto()
    CLUB    = auto()
    DIAMOND = auto()
    
class CardPlaces(Enum):
    FOUNDATION = 0
    CELL = 1
    WORKING_STACK = 2
    
class Card:
    
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
        
    def __repr__(self):
        return '{} - {}'.format(self.rank, self.suite)
    
    @property
    def value(self):
        return self.rank
    
    def validate_deck(cl):
        rl = list(map(lambda c: c.rank, cl))
        if any([True for r in range(13) if rl.count(r+1) != 4]):
            raise Exception('Rank validation failed in the deck', cl)
        sl = list(map(lambda c: c.suite.value, cl))
        if any([True for s in range(4) if sl.count(s+1) != 13]):
            raise Exception('Suite validation failed in the deck', cl)
        

class CardList:
    
    def __init__(self, card_place):
        self.card_place = card_place
        self.card_list = []
        
    def get_card_place(self):
        return self.card_place

class MoveLogic:
    
    def AlwaysTrue():
        def can_move():
            return True
        return can_move
    
    def AlwaysFalse():
        def can_move():
            return False
        return can_move

