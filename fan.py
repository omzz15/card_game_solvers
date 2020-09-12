# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 10:29:08 2020

@author: Om Patel
"""


from enum import Enum, auto
import random

#mode 0 is fast mode(just stops on first solution)
#mode 1 is thorough mode(runs through all iterations and picks the one with least steps)
mode = 0

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
        
    def get_num_of_suites(self, cards):
        suites = [0] * 4
        for card in cards:
            suites[card] += 1
        return suites
    
    def check_num_of_suites(self, cards):
        suites = self.get_num_of_suites(cards)
        if suites[0] == 13 and suites[1] == 13 and suites[2] == 13 and suites[3] == 13:
            return True
        return False
    
    def check_card_nums(self, cards):
        return len([False for i in range(1, 14) if cards.count(i) != 4]) == 0
        
    def get_card_lists(self):
        
        h = 0;#dont touch
        s = 1;#dont touch
        c = 2;#dont touch
        d = 3;#dont touch
        
        card_nums = [4,1,12,11,6,13,10,7,10,13,6,1,10,11,11,4,3,3,9,4,8,5,3,12,2,5,4,1,5,1,7,11,12,7,2,9,3,13,8,12,6,9,6,2,8,9,7,13,2,8,10,5]
        card_suites = [d,c,c,s,h,c,c,s,h,d,d,s,s,d,h,h,s,c,c,c,s,h,h,h,h,d,s,h,c,d,h,c,s,d,s,h,d,s,d,d,c,s,s,c,h,d,c,h,d,c,d,s]
        cards_per_pile = 4
        piles = 13
        
        cl = []# you dont need to put anythin in here 
        
        if len(card_nums) == 52 and len(card_suites) == 52 and self.check_num_of_suites(card_suites) and self.check_card_nums(card_nums):
            for x in range(piles):
                cl.append([])
                for y in range(cards_per_pile):    
                    if x*cards_per_pile + y < 52:
                        suite = card_suites[(x*cards_per_pile + y)]
                        if suite == 0:
                            cl[x].append(Card(card_nums[(x*cards_per_pile + y)], CardSuite.HEART))
                        if suite == 1:
                            cl[x].append(Card(card_nums[(x*cards_per_pile + y)], CardSuite.SPADE))
                        if suite == 2:
                            cl[x].append(Card(card_nums[(x*cards_per_pile + y)], CardSuite.CLUB))
                        if suite == 3:
                            cl[x].append(Card(card_nums[(x*cards_per_pile + y)], CardSuite.DIAMOND))
            return (True, cl)
        else:
            if len(card_nums) != 52: print(f"numbers not fully defined: only {len(card_nums)} numbers defined")
            if len(card_suites) != 52: print(f"suites not fully defined: only {len(card_suites)} suites defined")
            if self.check_num_of_suites(card_suites) == False:
                suites = self.get_num_of_suites(card_suites)
                print(f"{suites[0]} hearts, {suites[1]} spades, {suites[2]} clubs, {suites[3]} diamond") 
            if self.check_card_nums(card_nums) == False:
                for i in range(1,14):
                    print(f"the number of {i}s is {card_nums.count(i)}")
            return(False, None)
        
    def get_empty_foundation(self):
        return [[],[],[],[]]
    
    def solve(self):
        cards_defined = self.get_card_lists()[0]
        if cards_defined:
            itr = 10000
            total_itr = itr
            solutions = []
            best_solution = [None] * 300 
            while itr > 0:
                self.turns_since_foundation_changed = 0
                s = self.find_solution(self.get_card_lists()[1], self.get_empty_foundation(), list(), 50)
                print('{} - {}'.format(itr, s[0]))
                if s[0]:
                    if mode == 1: 
                        solutions.append(s[1])
                    else: return (f"found solution on iteration {itr}", s[1])
                itr -= 1
                
            for solution in solutions:
                if(len(solution) < len(best_solution)): best_solution = solution
                
            if best_solution[0] != None: return (f"{len(solutions)} solutions found, showing solution {solutions.index(best_solution) + 1} (best solution)", best_solution)
            else: return (f"could not find solution after {total_itr} iterations", []) 
        
        else: 
            return ("can not find solution because of improper deck definition", [])
    
    def find_solution(self, cardlist, fd, sol, max_moves_per_foundation_move):
        
        cards_to_put_in_foundations = self.find_cards_to_put_in_foundations(cardlist, fd)
        #print(cards_to_put_in_foundations)
        cards_to_move_between_card_lists = self.find_cards_to_move_between_card_lists(cardlist)
        #print(cards_to_move_between_card_lists)
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
           
    def find_cards_to_put_in_foundations(self, cardlist, fd):
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
                if cl_from != []: 
                    if cl_to != []:
                        if cl_from[-1].value + 1 == cl_to[-1].value and cl_from[-1].suite == cl_to[-1].suite:
                            card_list_from.append(cl_from_num)
                            card_list_to.append(cl_to_num)
                    elif cl_from[-1].value == 13:
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
    

s = Solution()
sol = s.solve()
print(sol[0])
for i in sol[1]:
    print(i)
