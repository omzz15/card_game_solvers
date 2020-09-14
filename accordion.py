# accordian, decade, eliminator, royal marriage, seven up
# addiction, three pharoahs, streets & alleys, all in a row, 

from card import Card, CardSuite
import random

class CardGameSolver:
    pass
    
class Solution:
    
    def __init__(self, cardlist):
        self.card_list = cardlist

    def solve_deep(self):
        s = self.find_solution_deep(self.card_list.copy(), list())
        print('{} - {}'.format(s[0], s[1]))
        return s[1]
    
    def solve_random(self):
        itr = 2
        while itr > 0:
            s = self.find_solution_random(self.card_list.copy(), list())
            print('{} - {}'.format(itr, s[0]))
            #input()
            if s[0]: return s[1]
            itr -= 1
        return []

    def find_solution_move(self, cl, sol, f, t):
        cl[f], cl[t] = cl[t], cl[f]
        c = cl[f]
        cl = cl[0:f]+cl[f+1:]
        return self.find_solution_deep(cl, sol+[c])
        
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
    
cl = list()
cl.append(Card( 3, CardSuite.SPADE))
cl.append(Card(12, CardSuite.DIAMOND))
cl.append(Card(10, CardSuite.DIAMOND))
cl.append(Card( 2, CardSuite.DIAMOND))
cl.append(Card( 9, CardSuite.DIAMOND))
cl.append(Card( 9, CardSuite.CLUB))
cl.append(Card(12, CardSuite.SPADE))
cl.append(Card(11, CardSuite.SPADE))
cl.append(Card( 2, CardSuite.SPADE))
cl.append(Card(11, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.SPADE))
cl.append(Card( 1, CardSuite.SPADE))
cl.append(Card( 2, CardSuite.HEART))

cl.append(Card( 6, CardSuite.HEART))
cl.append(Card( 9, CardSuite.HEART))
cl.append(Card( 4, CardSuite.HEART))
cl.append(Card( 4, CardSuite.DIAMOND))
cl.append(Card( 7, CardSuite.SPADE))
cl.append(Card( 5, CardSuite.DIAMOND))
cl.append(Card(10, CardSuite.HEART))
cl.append(Card( 8, CardSuite.CLUB))
cl.append(Card( 8, CardSuite.SPADE))
cl.append(Card(12, CardSuite.HEART))
cl.append(Card( 4, CardSuite.SPADE))
cl.append(Card( 3, CardSuite.DIAMOND))
cl.append(Card( 8, CardSuite.HEART))

cl.append(Card( 1, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.HEART))
cl.append(Card(13, CardSuite.DIAMOND))
cl.append(Card( 6, CardSuite.DIAMOND))
cl.append(Card(10, CardSuite.SPADE))
cl.append(Card( 3, CardSuite.CLUB))
cl.append(Card(13, CardSuite.HEART))
cl.append(Card( 2, CardSuite.CLUB))
cl.append(Card( 9, CardSuite.SPADE))
cl.append(Card( 7, CardSuite.DIAMOND))
cl.append(Card( 1, CardSuite.DIAMOND))
cl.append(Card( 5, CardSuite.CLUB))
cl.append(Card(11, CardSuite.HEART))

cl.append(Card( 6, CardSuite.SPADE))
cl.append(Card(11, CardSuite.DIAMOND))
cl.append(Card( 8, CardSuite.DIAMOND))
cl.append(Card( 7, CardSuite.CLUB))
cl.append(Card(12, CardSuite.CLUB))
cl.append(Card(10, CardSuite.CLUB))
cl.append(Card(13, CardSuite.SPADE))
cl.append(Card( 4, CardSuite.CLUB))
cl.append(Card( 7, CardSuite.HEART))
cl.append(Card( 3, CardSuite.HEART))
cl.append(Card( 6, CardSuite.CLUB))
cl.append(Card(13, CardSuite.CLUB))
cl.append(Card( 1, CardSuite.HEART))

Card.validate_deck(cl)
s = Solution(cl)
sol = s.solve_deep()
for i in sol:
    print(i)
