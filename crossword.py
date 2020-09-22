# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 16:54:34 2020

@author: gauta
"""
from card import Card, CardSuite

class Solution:
    
    def __init__(self, cl, ch, cc):
        self.cl = cl
        self.ch = ch
        self.ws = [[None]*7 for i in range(7)]
        self.ws[3][3] = c
        
    def is_solved(self):
        # is any slot empty??
        for i in range(7):
            for j in range(7):
                if self.ws[i][j] == None:
                    return False
        # is number card sum in any row & column not even??
        for i in range(7):
            rsum, csum = 0
            for j in range(7):
                if self.ws[i][j].rank < 11: rsum += self.ws[i][j].rank
                if self.ws[j][i].rank < 11: csum += self.ws[j][i].rank
            if rsum%2 != 0 or csum%2 != 0: return False
    
s, d, c, h = CardSuite.get_suite_num_vars()

card_nums = [
    12,  6, 10,  3,  5,  5, 11,  1,  6,  4,  8, 12,  7,
     2,  9, 11,  8, 11,  7,  9,  8,  2, 12,  7,  8,  2,
     9, 10,  1,  5, 12,  4,  6, 13,  4,  3,  6, 10, 10,
    13,  3, 11,  1,  9,  7, 13,  4,  1,  2,  3,  5, 13]
card_suites = [
    h,d,d,d,d,s,d,d,s,d,s,c,s,
    d,c,c,d,h,c,h,c,c,s,d,h,s,
    d,s,h,c,d,s,c,c,h,h,h,h,c,
    d,c,s,c,s,h,s,c,s,h,s,h,h]

card_list = Card.get_card_lists(card_nums, card_suites, 2)
cl = card_list[0]
ch = card_list[1]
cc = Card(1, CardSuite.DIAMOND)

