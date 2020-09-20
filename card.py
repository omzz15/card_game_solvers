# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 16:34:54 2020

@author: q774283
"""

from enum import Enum
import math

class CardSuite(Enum):
    SPADE   = 1
    DIAMOND = 2
    CLUB    = 3
    HEART   = 4
    
    def get_suite_by_chr(schr):
        for n in CardSuite._member_map_:
            if n[0] == schr.upper(): return CardSuite._member_map_[n]
        raise Exception(f'Unknown suite {schr}')

    def get_suite_by_num(snum):
        for n in CardSuite._value2member_map_:
            if n == snum: return CardSuite._value2member_map_[n]
        raise Exception(f'Unknown suite {snum}')
    
    def get_suite_num_vars():
        return (CardSuite.SPADE.value, CardSuite.DIAMOND.value, CardSuite.CLUB.value, CardSuite.HEART.value)
    
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
        
    def get_card_lists(card_nums, card_suites, piles=4, num_of_cards=None, suite_as_num=True):
        if len(card_nums) != len(card_suites):
            raise Exception('No of cards in rank and suite list do not match')
        if num_of_cards == None:
            num_of_cards = len(card_nums)
        else:
            if num_of_cards != len(card_nums):
                raise Exception('No of cards in rank do not match')
            if num_of_cards != len(card_suites):
                raise Exception('No of cards in suites do not match')
            
        cards_per_pile = math.ceil(len(card_nums) / piles)
        
        cl = []
        for x in range(piles):
            cl.append([])
            for y in range(cards_per_pile):
                idx = x*cards_per_pile + y
                if idx < num_of_cards:
                    if suite_as_num:
                        cl[x].append(Card(card_nums[idx], CardSuite.get_suite_by_num(card_suites[idx])))
                    else:
                        cl[x].append(Card(card_nums[idx], CardSuite.get_suite_by_chr(card_suites[idx])))
        return cl

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

