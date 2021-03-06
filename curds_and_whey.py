# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:03:31 2020

@author: Om Patel
"""

##############################
   ##binned for right now##    
##############################


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
    
    @property
    def value(self):
        return self.rank
    
class Solution:
    
    def __init__(self):
        self.turns_since_foundation_changed = 0
        
    def get_card_lists(self):
        cl1 = list()
        cl1.append(Card( 9, CardSuite.CLUB))
        cl1.append(Card( 9, CardSuite.DIAMOND))
        cl1.append(Card(10, CardSuite.HEART))
        cl1.append(Card(10, CardSuite.DIAMOND))
        
        cl2 = list()
        cl2.append(Card( 1, CardSuite.CLUB))
        cl2.append(Card( 4, CardSuite.CLUB))
        cl2.append(Card( 3, CardSuite.DIAMOND))
        cl2.append(Card(10, CardSuite.SPADE))
        
        cl3 = list()
        cl3.append(Card(11, CardSuite.HEART))
        cl3.append(Card( 6, CardSuite.CLUB))
        cl3.append(Card( 9, CardSuite.SPADE))
        cl3.append(Card(12, CardSuite.SPADE))
        
        cl4 = list()
        cl4.append(Card(13, CardSuite.CLUB))
        cl4.append(Card(12, CardSuite.CLUB))
        cl4.append(Card(12, CardSuite.DIAMOND))
        cl4.append(Card( 3, CardSuite.CLUB))
        
        cl5 = list()
        cl5.append(Card( 4, CardSuite.SPADE))
        cl5.append(Card(11, CardSuite.SPADE))
        cl5.append(Card( 8, CardSuite.CLUB))
        cl5.append(Card(12, CardSuite.HEART))
        
        cl6 = list()
        cl6.append(Card( 8, CardSuite.DIAMOND))
        cl6.append(Card( 5, CardSuite.SPADE))
        cl6.append(Card( 4, CardSuite.HEART))
        cl6.append(Card( 4, CardSuite.DIAMOND))
        
        cl7 = list()
        cl7.append(Card(10, CardSuite.CLUB))
        cl7.append(Card( 2, CardSuite.SPADE))
        cl7.append(Card( 1, CardSuite.HEART))
        cl7.append(Card( 2, CardSuite.CLUB))
        
        cl8 = list()
        cl8.append(Card(11, CardSuite.DIAMOND))
        cl8.append(Card( 6, CardSuite.DIAMOND))
        cl8.append(Card( 8, CardSuite.HEART))
        cl8.append(Card( 3, CardSuite.HEART))
        
        cl9 = list()
        cl9.append(Card( 7, CardSuite.HEART))
        cl9.append(Card( 5, CardSuite.CLUB))
        cl9.append(Card( 7, CardSuite.SPADE))
        cl9.append(Card( 2, CardSuite.HEART))
        
        cl10 = list()
        cl10.append(Card(13, CardSuite.SPADE))
        cl10.append(Card( 1, CardSuite.DIAMOND))
        cl10.append(Card( 3, CardSuite.SPADE))
        cl10.append(Card( 5, CardSuite.HEART))
        
        cl11 = list()
        cl11.append(Card( 1, CardSuite.SPADE))
        cl11.append(Card(11, CardSuite.CLUB))
        cl11.append(Card( 2, CardSuite.DIAMOND))
        cl11.append(Card( 9, CardSuite.HEART))
        
        cl12 = list()
        cl12.append(Card(13, CardSuite.HEART))
        cl12.append(Card( 5, CardSuite.DIAMOND))
        cl12.append(Card( 8, CardSuite.SPADE))
        cl12.append(Card( 6, CardSuite.SPADE))
        
        cl13 = list()
        cl13.append(Card(13, CardSuite.DIAMOND))
        cl13.append(Card( 7, CardSuite.CLUB))
        cl13.append(Card( 6, CardSuite.HEART))
        cl13.append(Card( 7, CardSuite.DIAMOND))
        
        return [cl1, cl2, cl3, cl4, cl5,  cl6, cl7, cl8, cl9, cl10, cl11, cl12, cl13]
        
    def get_empty_foundation(self):
        return [[],[],[],[]]
    
    def solve(self):
        itr = 10000
        solutions = []
        best_solution = [None] * 300 
        while itr > 0:
            self.turns_since_foundation_changed = 0
            s = self.find_solution(self.get_card_lists(), self.get_empty_foundation(), list(), 50)
            print('{} - {}'.format(itr, s[0]))
            if s[0]: 
                solutions.append(s[1])
            itr -= 1
            
        for solution in solutions:
            if(len(solution) < len(best_solution)): best_solution = solution
        
        return best_solution
    
    def find_solution(self, cardlist, fd, sol, max_moves_per_foundation_move):
        
        cards_to_put_in_foundations = self.find_cards_to_put_in_foundations(cardlist, fd)
       # print(cards_to_put_in_foundations)
        cards_to_move_between_card_lists = self.find_cards_to_move_between_card_lists(cardlist)
       # print(cards_to_move_between_card_lists)
        if self.find_cards_left_in_all_lists(cardlist) == 0: return (True, sol)
        if cards_to_put_in_foundations[0] == False:  
            if cards_to_move_between_card_lists[0] == False: return(False, sol)
            self.turns_since_foundation_changed += 1
            if self.turns_since_foundation_changed > max_moves_per_foundation_move: return(False, sol)
        else: self.turns_since_foundation_changed = 0
        
        
        
        if cards_to_put_in_foundations[0] == True:
            random_num = random.randint(0, len(cards_to_put_in_foundations[1]) - 1)
            from_card_pile = cards_to_put_in_foundations[1][random_num]
            to_foundation = cards_to_put_in_foundations[2][random_num]
            
            sol.append(f"move card ({cardlist[from_card_pile][-1]}) from list: {from_card_pile + 1} to foundation: {to_foundation + 1}")
            
            fd[to_foundation].append(cardlist[from_card_pile][-1])
            del  cardlist[from_card_pile][-1]
            
        else:
            random_num = random.randint(0, len(cards_to_move_between_card_lists[1]) - 1)
            from_list = cards_to_move_between_card_lists[1][random_num] 
            to_list = cards_to_move_between_card_lists[2][random_num]
            
            sol.append(f"move card ({cardlist[from_list][-1]}) from list: {from_list + 1} to list: {to_list + 1}")
            
            cardlist[to_list].append(cardlist[from_list][-1])
            del  cardlist[from_list][-1]
            
        return self.find_solution(cardlist, fd, sol, max_moves_per_foundation_move)
           
    def find_cards_to_put_in_empty_slot(self, cardlist, fd):
       cards = []
       foundations = []
       cl_num = 0
       fd_num = 0
       
       for card_list in cardlist:
           for foundation in fd:
              if card_list != []:
                  if foundation != []:
                      if card_list[-1].suite == foundation[-1].suite and card_list[-1].rank - 1 == foundation[-1].rank:
                            cards.append(cl_num)
                            foundations.append(fd_num)
                  elif(card_list[-1].rank == 1):
                      cards.append(cl_num)
                      foundations.append(fd_num)
              fd_num += 1
           cl_num += 1
           fd_num = 0
       
       if cards == []: return (False, None, None)
       else: return (True, cards, foundations)
      
    def find_cards_to_move_between_card_lists(self, cardlist):
        card_list_from = []
        card_list_to = []
        cl_from_num = 0
        cl_to_num = 0
  
        for cl_from in cardlist:
            for cl_to in cardlist:
                if cl_from != [] and cl_to != []:
                    if(cl_from[-1].value + 1 == cl_to[-1].value):
                        card_list_from.append(cl_from_num)
                        card_list_to.append(cl_to_num)
                cl_to_num += 1
            cl_from_num += 1
            cl_to_num = 0
           
        if card_list_from == []: return(False, None, None)
        else: return(True, card_list_from, card_list_to)
    
    def find_cards_left_in_all_lists(self, cl):
        total = 0
        for cards in cl:
            if cards != []: total += len(cards)
        return total
    
    def clear

s = Solution()
sol = s.solve()
for i in sol:
    print(i)

