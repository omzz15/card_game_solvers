# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 20:46:40 2020

@author: Om Patel
"""

from card import Card, CardSuite
import random

    
class Solution:
    
    def __init__(self, cl_list):
        self.card_lists = cl_list
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
    
    def neighbor(c1, other):
        if(other == None or c1 == None): return False
        if(c1.rank + 1 == other.rank or c1.rank - 1 == other.rank): return True
        elif((c1.rank == 13 and other.rank == 1) or(c1.rank == 1 and other.rank == 13)): return True
        else: return False
    
    def find_card_for_all_foundations(self, card_lists):
        cards = []
        foundations = []
        cl = 0
        f = 0
        
        for foundation in self.foundations:
            for card_list in card_lists:
                if card_list != []:
                    if foundation != []:
                        if(Solution.neighbor(card_list[-1], foundation[-1])): 
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
                    if Solution.neighbor(foundation_1[-1], foundation_2[-1]):
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


s, d, c, h = CardSuite.get_suite_num_vars()

card_nums = [4,1,12,11,6,13,10,7,10,13,6,1,10,11,11,4,3,3,9,4,8,5,3,12,2,5,4,1,5,1,7,11,12,7,2,9,3,13,8,12,6,9,6,2,8,9,7,13,2,8,10,5]
card_suites = [d,c,c,s,h,c,c,s,h,d,d,s,s,d,h,h,s,c,c,c,s,h,h,h,h,d,s,h,c,d,h,c,s,d,s,h,d,s,d,d,c,s,s,c,h,d,c,h,d,c,d,s]
cl_list = Card.get_card_lists(card_nums, card_suites)

s = Solution(cl_list)
sol = s.solve()
for i in sol:
    print(i)
