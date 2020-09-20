# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:46:40 2020

@author: Om Patel
"""

from enum import Enum, auto
import random

class CardSuite(Enum):
    HEART   = auto()
    SPADE   = auto()
    CLUB    = auto()
    DIAMOND = auto()
    
class Card:
    
    def __init__(self, rank, suite):
        self.rank = rank
        self.suite = suite
        
    def __repr__(self):
        return '{} - {}'.format(self.rank, self.suite)
    def neighbor(self, other):
        if(other == None): return False
        if(self.rank + 1 == other.rank or self.rank - 1 == other.rank): return True
        elif((self.rank == 13 and other.rank == 1) or(self.rank == 1 and other.rank == 13)): return True
        else: return False
    @property
    def value(self):
        return self.rank
    
class Solution:
    
    def __init__(self, cl1, c12, cl3, cl4):
        self.card_lists = [cl1, cl2, cl3, cl4]
        self.foundations = [[], [], [], [], [], []]
    
    def solve(self):
        itr = 100
        while itr > 0:
            self.foundations = [[], [], [], [], [], []]
            s = self.find_solution(self.card_lists.copy(), list())
            print('{} - {}'.format(itr, s[0]))
            if s[0]: return s[1]
            itr -= 1
        return []
    
    """ 
    def find_card_for_foundation(self, foundation):
        for card_list in self.card_lists:
            if(card_list[-1].neighbor(foundation[-1])): return (True, card_list[-1])
        return (False, None)
    """
    
    def find_card_for_all_foundations(self, card_lists):
        cards = []
        foundations = []
        cl = 0
        f = 0
        
        for foundation in self.foundations:
            for card_list in card_lists:
                if card_list != []:
                    if foundation != []:
                        if(card_list[-1].neighbor(foundation[-1])): 
                            cards.append(cl)
                            foundations.append(f)
                    else:
                        cards.append(cl)
                        foundations.append(f)
                    
                cl += 1
            f += 1
            cl = 0
             
        if cards == []: return(False, None, None)
        else: return (True, cards, foundations)
    
    def find_card_to_move_between_foundations(self):
        foundation_from = []
        foundation_to = []
        ff = 0
        ft = 0
        
        for foundation_1 in self.foundations:
            for foundation_2 in self.foundations:
                if foundation_1 != [] and foundation_2 != []:
                    if foundation_1[-1].neighbor(foundation_2[-1]):
                        foundation_from.append(ff)
                        foundation_to.append(ft)
                ft += 1
            ff += 1
            ft = 0
            
        if foundation_from == []: return (False, None, None)
        else: return (True, foundation_from, foundation_to)
    
    def check_if_cards_are_gone(self , card_lists):
        lists_empty = 0
        for card_list in card_lists:
            if card_list == []: lists_empty += 1
        if lists_empty == 4: return True
        else: return False
    
    def find_solution(self, card_lists, sol):
        #recurtion break checks:
        all_movable_cards = self.find_card_for_all_foundations(card_lists)
        all_movable_foundation_cards = self.find_card_to_move_between_foundations()
        
        if  all_movable_cards[0] == False and  all_movable_foundation_cards[0] == False: return (False, sol) 
        if self.check_if_cards_are_gone(card_lists): return (True, sol) 

        card_list = card_lists
        solution = sol
                
        if all_movable_cards[0] == False:
            random_num = random.randint(0, len(all_movable_foundation_cards[1]) - 1)
            from_foundation_num = all_movable_foundation_cards[1][random_num]
            from_foundation_card = self.foundations[from_foundation_num][-1]
            to_foundation_num = all_movable_foundation_cards[2][random_num]
            
            del self.foundations[from_foundation_num][-1]
            self.foundations[to_foundation_num].append(from_foundation_card)
            solution.append((f'move card {from_foundation_card} from foundation {from_foundation_num + 1} to foundation {to_foundation_num + 1}'))
        else:
            random_num = random.randint(0, len(all_movable_cards[1]) - 1)
            card_list_num = all_movable_cards[1][random_num]
            card_list_card = card_lists[card_list_num][-1]
            foundation_to = all_movable_cards[2][random_num]
            
            del card_lists[card_list_num][-1]
            self.foundations[foundation_to].append(card_list_card)
            solution.append((f"move card {card_list_card} from card list {card_list_num + 1} to foundation {foundation_to + 1}"))
        
        return self.find_solution(card_list, solution)

#################################
#input deck info(suite optional)#
#################################        
    
cl1 = list()
cl1.append(Card(13, CardSuite.DIAMOND))
cl1.append(Card(11, CardSuite.SPADE))
cl1.append(Card( 5, CardSuite.SPADE))
cl1.append(Card( 3, CardSuite.SPADE))
cl1.append(Card( 6, CardSuite.DIAMOND))
cl1.append(Card( 9, CardSuite.SPADE))
cl1.append(Card(10, CardSuite.SPADE))
cl1.append(Card( 8, CardSuite.HEART))
cl1.append(Card( 9, CardSuite.HEART))
cl1.append(Card(11, CardSuite.DIAMOND))
cl1.append(Card( 4, CardSuite.SPADE))
cl1.append(Card( 8, CardSuite.DIAMOND))
cl1.append(Card( 5, CardSuite.SPADE))

cl2 = list()
cl2.append(Card(12, CardSuite.CLUB))
cl2.append(Card( 8, CardSuite.SPADE))
cl2.append(Card(10, CardSuite.SPADE))
cl2.append(Card( 7, CardSuite.CLUB))
cl2.append(Card( 7, CardSuite.DIAMOND))
cl2.append(Card( 4, CardSuite.SPADE))
cl2.append(Card( 2, CardSuite.CLUB))
cl2.append(Card( 5, CardSuite.CLUB))
cl2.append(Card( 9, CardSuite.CLUB))
cl2.append(Card( 3, CardSuite.SPADE))
cl2.append(Card( 7, CardSuite.HEART))
cl2.append(Card(10, CardSuite.DIAMOND))
cl2.append(Card(12, CardSuite.DIAMOND))

cl3 = list()
cl3.append(Card( 5, CardSuite.SPADE))
cl3.append(Card( 6, CardSuite.HEART))
cl3.append(Card( 1, CardSuite.SPADE))
cl3.append(Card( 6, CardSuite.CLUB))
cl3.append(Card( 4, CardSuite.CLUB))
cl3.append(Card(13, CardSuite.CLUB))
cl3.append(Card(11, CardSuite.CLUB))
cl3.append(Card( 6, CardSuite.CLUB))
cl3.append(Card( 7, CardSuite.DIAMOND))
cl3.append(Card( 9, CardSuite.HEART))
cl3.append(Card(12, CardSuite.CLUB))
cl3.append(Card(12, CardSuite.DIAMOND))
cl3.append(Card( 1, CardSuite.HEART))

cl4 = list()
cl4.append(Card(13, CardSuite.DIAMOND))
cl4.append(Card( 2, CardSuite.HEART))
cl4.append(Card( 2, CardSuite.DIAMOND))
cl4.append(Card(10, CardSuite.HEART))
cl4.append(Card( 1, CardSuite.HEART))
cl4.append(Card( 1, CardSuite.HEART))
cl4.append(Card( 4, CardSuite.DIAMOND))
cl4.append(Card(11, CardSuite.CLUB))
cl4.append(Card( 3, CardSuite.HEART))
cl4.append(Card( 8, CardSuite.CLUB))
cl4.append(Card( 3, CardSuite.DIAMOND))
cl4.append(Card(13, CardSuite.HEART))
cl4.append(Card( 2, CardSuite.HEART))

s = Solution(cl1, cl2, cl3, cl4)
sol = s.solve()
for i in sol:
    print(i)
