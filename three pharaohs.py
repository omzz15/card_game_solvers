# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 13:05:40 2020

@author: Om Patel
"""


from card import Card, CardSuite
import random

    
class Solution:
    
    def __init__(self):
        self.card_list = self.get_cards()

    def make_pharaoh(self, p_cards, p_size):
        output = []
        for i in range(p_size):
            arr = []
            for x in range(i + 1):
                
                value = 0
                for v in range(i):
                    value += v
                value += (x)
                
                if(p_cards[1][value] == 0): arr.append(Card( p_cards[0][value], CardSuite.HEART))
                elif(p_cards[1][value] == 1): arr.append(Card( p_cards[0][value], CardSuite.SPADE))
                elif(p_cards[1][value] == 2): arr.append(Card( p_cards[0][value], CardSuite.CLUB))
                elif(p_cards[1][value] == 3): arr.append(Card( p_cards[0][value], CardSuite.DIAMOND))
                else: raise Exception('suite value not recognized', p_cards[1][value])
            output.append(arr)
        return output

    def get_cards(self):
        
        h = 0;#dont touch
        s = 1;#dont touch
        c = 2;#dont touch
        d = 3;#dont touch
        
        p1_values = []
        p1_suites = [h,s,c,d]
        p1 = self.make_pharaoh([p1_values, p1_suites], 4)
        
        p2_values = []
        p2_suites = []
        p2 = self.make_pharaoh([p2_values, p2_suites], 6)
        
        p3_values = []
        p3_suites = []
        p3 = self.make_pharaoh([p3_values, p3_suites], 6)
        
        return [p1,p2,p3];

    def get_open_cards(self, p_list):
        open_cards = []
        for tier in range(len(p_list)):
             for card in range(len(p_list[tier])):
                 if(p_list[tier][card] != None):
                     if(tier == len(p_list) - 1): open_cards.append([tier, card])
                     elif():
                 
        

    def solve_deep(self):
        s = self.find_solution_deep(self.card_list.copy(), list())
        print('{} - {}'.format(s[0], s[1]))
        return s[1]
    
    def solve_random(self):
        itr = 100
        while itr > 0:
            s = self.find_solution_random(self.card_list.copy(), list())
            print('{} - {}'.format(itr, s[0]))
            #input()
            if s[0]: return s[1]
            itr -= 1
        return []
        
    def find_solution_deep(self, cl, sol):
        #print(cl)
        #print(sol)
        #input()
        if len(cl) == 0: return (False, sol)
        if len(cl) == 1: return (True, sol)
        rnk_sol, suit_sol = self.find_all_moves(cl)
        for f, t in rnk_sol:
            found, new_sol = self.find_solution_move(cl, sol, f, t)
            if found is not None:
                return (found, new_sol)
        for f, t in suit_sol:
            found, new_sol = self.find_solution_move(cl, sol, f, t)
            if found is not None:
                return (found, new_sol)
        return (None, sol)
    
    def find_solution_random(self, cl, sol):
        #print(cl)
        #print(sol)
        #input()
        if len(cl) == 0: return (False, sol)
        if len(cl) == 1: return (True, sol)
        f, t = self.find_random_move(cl)
        if f == -1 or t == -1:
            return (False, sol)
        cl[f], cl[t] = cl[t], cl[f]
        sol.append(cl[f])
        cl = cl[0:f]+cl[f+1:]
        return self.find_solution_random(cl, sol)
        
    def find_all_moves(self, cl):
        rnk_sol = []
        suit_sol = []
        for f in range(len(cl)):
            t = self.find_to(cl, f, True, False)
            if t >= 0:
                rnk_sol.append((f, t))
            t = self.find_to(cl, f, False, True)
            if t >= 0:
                suit_sol.append((f, t))
        return (rnk_sol, suit_sol)
        
    def find_random_move(self, cl):
        rnk_sol, suit_sol = self.find_all_moves(cl)
        select = lambda l: l[random.randint(0, len(l)-1)]
        if len(rnk_sol) == 0 and len(rnk_sol) == 0:
            return (-1, -1)
        elif len(rnk_sol) == 0:
            return select(suit_sol)
        elif len(suit_sol) == 0:
            return select(rnk_sol)
        else:
            if bool(random.getrandbits(1)):
                return select(suit_sol)
            else:
                return select(rnk_sol)
        
    def find_to(self, cl, f, com_rank, com_suite):
        if com_rank:
            if f>2 and cl[f].rank == cl[f-3].rank:
                return f-3
            if f>0 and cl[f].rank == cl[f-1].rank:
                return f-1
        if com_suite:
            if f>2 and cl[f].suite == cl[f-3].suite:
                return f-3
            if f>0 and cl[f].suite == cl[f-1].suite:
                return f-1
        return -1        


s = Solution()
sol = s.solve_deep()
for i in sol:
    print(i)
