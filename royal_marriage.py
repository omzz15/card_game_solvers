from card import Card, CardSuite
import random
    
class Solution:
    
    def __init__(self, cardlist):
        self.card_list = cardlist
    
    def solve(self):
        itr = 500
        while itr > 0:
            s = self.find_solution(self.card_list.copy(), list())
            print('{} - {}'.format(itr, s[0]))
            #input()
            if s[0]: return s[1]
            itr -= 1
        return []
    
    def find_solution(self, cl, sol):
        #print(cl)
        #print(sol)
        #input()
        if len(cl) == 2: return (True, sol)
        if len(cl) < 3: return (False, sol)
        if len(cl) <= 25:
            t = -1
            for f in range(len(cl)):
                t = self.find_to(cl, f, True, True)
                if t > f: break
            if t > f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f+1]+cl[t:]
                return self.find_solution(cl, sol)
            else:
                return (False, sol)
        else:
            f = random.randint(0, len(cl)-1)
            rf = bool(random.getrandbits(1))
            t = self.find_to(cl, f, rf, not(rf))
            if t > f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f+1]+cl[t:]
            return self.find_solution(cl, sol)
        
    def find_to(self, cl, f, com_rank, com_suite):
        for t in range(f+2, f+4):
            if t >= len(cl): break
            if cl[f].rank == cl[t].rank and com_rank:
                return t
            t += 1
        for t in range(f+2, f+4):
            if t >= len(cl): break
            if cl[f].suite == cl[t].suite and com_suite:
                return t
            t += 1
        return -1
        
    
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
cl = Card.get_card_lists(card_nums, card_suites, 1)[0]

Card.validate_deck(cl)
s = Solution(cl)
sol = s.solve()
for i in sol:
    print(i)
