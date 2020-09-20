from card import CardSuite, Card
import random

class CardExt(Card):
    
    def __init__(self, rank, suite):
        super().__init__(rank, suite)
        
    @property
    def value(self):
        if self.rank > 10: return 10
        return self.rank
    
class Solution:
    
    def __init__(self, cardlist):
        self.card_list = cardlist
    
    def solve(self):
        itr = 100
        while itr > 0:
            s = self.find_solution(self.card_list.copy(), list())
            print('{} - {}'.format(itr, s[0]))
            if s[0]: return s[1]
            itr -= 1
        return []
    
    def find_solution(self, cl, sol):
        if len(cl) == 0: return (True, sol)
        if len(cl) == 1: return (False, sol)
        value = self.calc_sum(cl)
        if value in (10, 20, 30):
            sol.append((cl[0], cl[-1]))
            return (True, sol)
        if value < 10:
            return (False, sol)
        if len(cl) <= 15:
            t = -1
            for f in range(len(cl)):
                t = self.find_to(cl, f)
                if t > f: break
            if t > f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f]+cl[t+1:]
                return self.find_solution(cl, sol)
            else:
                return (False, sol)
        else:
            f = random.randint(0, len(cl)-1)
            t = self.find_to(cl, f)
            if t > f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f]+cl[t+1:]
            return self.find_solution(cl, sol)
        
    def find_to(self, cl, f):
        s = cl[f].value
        t = f+1
        while t < len(cl):
            s += cl[t].value
            if s in (10, 20, 30):
                return t
            if s > 30:
                break
            t += 1
        return -1
        
    def calc_sum(self, cl):
        value = 0
        for c in cl:
            value += c.value
            if value > 30:
                break
        return value
    
cl = list()
cl.append(CardExt( 7, CardSuite.DIAMOND))
cl.append(CardExt( 5, CardSuite.CLUB))
cl.append(CardExt( 5, CardSuite.SPADE))
cl.append(CardExt(11, CardSuite.HEART))
cl.append(CardExt( 3, CardSuite.DIAMOND))
cl.append(CardExt( 4, CardSuite.HEART))
cl.append(CardExt(12, CardSuite.HEART))
cl.append(CardExt( 8, CardSuite.DIAMOND))
cl.append(CardExt(10, CardSuite.HEART))
cl.append(CardExt(10, CardSuite.CLUB))
cl.append(CardExt( 2, CardSuite.SPADE))
cl.append(CardExt( 1, CardSuite.SPADE))
cl.append(CardExt(10, CardSuite.SPADE))

cl.append(CardExt( 7, CardSuite.CLUB))
cl.append(CardExt(10, CardSuite.DIAMOND))
cl.append(CardExt( 8, CardSuite.HEART))
cl.append(CardExt( 2, CardSuite.DIAMOND))
cl.append(CardExt(12, CardSuite.SPADE))
cl.append(CardExt(11, CardSuite.SPADE))
cl.append(CardExt( 9, CardSuite.HEART))
cl.append(CardExt( 4, CardSuite.DIAMOND))
cl.append(CardExt( 9, CardSuite.CLUB))
cl.append(CardExt(11, CardSuite.DIAMOND))
cl.append(CardExt(13, CardSuite.SPADE))
cl.append(CardExt(13, CardSuite.DIAMOND))
cl.append(CardExt( 2, CardSuite.HEART))

cl.append(CardExt( 8, CardSuite.CLUB))
cl.append(CardExt( 7, CardSuite.SPADE))
cl.append(CardExt(11, CardSuite.CLUB))
cl.append(CardExt( 3, CardSuite.SPADE))
cl.append(CardExt(13, CardSuite.CLUB))
cl.append(CardExt( 1, CardSuite.CLUB))
cl.append(CardExt( 2, CardSuite.CLUB))
cl.append(CardExt( 3, CardSuite.CLUB))
cl.append(CardExt( 6, CardSuite.CLUB))
cl.append(CardExt( 1, CardSuite.HEART))
cl.append(CardExt( 6, CardSuite.HEART))
cl.append(CardExt( 6, CardSuite.DIAMOND))
cl.append(CardExt( 5, CardSuite.DIAMOND))

cl.append(CardExt(13, CardSuite.HEART))
cl.append(CardExt( 9, CardSuite.DIAMOND))
cl.append(CardExt(12, CardSuite.DIAMOND))
cl.append(CardExt( 7, CardSuite.HEART))
cl.append(CardExt( 4, CardSuite.CLUB))
cl.append(CardExt(12, CardSuite.CLUB))
cl.append(CardExt( 5, CardSuite.HEART))
cl.append(CardExt( 3, CardSuite.HEART))
cl.append(CardExt( 1, CardSuite.DIAMOND))
cl.append(CardExt( 4, CardSuite.SPADE))
cl.append(CardExt( 6, CardSuite.SPADE))
cl.append(CardExt( 9, CardSuite.SPADE))
cl.append(CardExt( 8, CardSuite.SPADE))

Card.validate_deck(cl)
s = Solution(cl)
sol = s.solve()
for i in sol:
    print(i)
