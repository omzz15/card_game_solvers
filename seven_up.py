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
        #print(cl)
        #print(sol)
        #input()
        if len(cl) == 0: return (True, sol)
        value = self.calc_sum(cl)
        if value < 7: return (False, sol)
        if len(cl) == 1:
            if cl[0].value == 7:
                sol.append((cl[0], cl[0]))
                return (True, sol)
            else:
                return (False, sol)
        if len(cl) in (2, 3, 4) and value%7 == 0: 
            sol.append((cl[0], cl[-1]))
            return (True, sol)
        if len(cl) <= 10:
            t = -1
            for f in range(len(cl)):
                t = self.find_to(cl, f)
                if t >= f: break
            if t > f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f]+cl[t+1:]
                return self.find_solution(cl, sol)
            else:
                return (False, sol)
        else:
            f = random.randint(0, len(cl)-1)
            t = self.find_to(cl, f)
            if t >= f:
                sol.append((cl[f], cl[t]))
                cl = cl[0:f]+cl[t+1:]
            return self.find_solution(cl, sol)
        
    def find_to(self, cl, f):
        s = 0
        for t in range(f, f+4):
            if t >= len(cl): break
            s += cl[t].value
            if s%7 == 0:
                return t
            t += 1
        return -1
        
    def calc_sum(self, cl):
        value = 0
        for c in cl:
            value += c.value
            if value > 52:
                break
        return value
    
cl = list()
cl.append(Card( 4, CardSuite.CLUB))
cl.append(Card(10, CardSuite.CLUB))
cl.append(Card( 4, CardSuite.DIAMOND))
cl.append(Card( 8, CardSuite.SPADE))
cl.append(Card(10, CardSuite.HEART))
cl.append(Card( 3, CardSuite.HEART))
cl.append(Card(12, CardSuite.SPADE))
cl.append(Card( 9, CardSuite.DIAMOND))
cl.append(Card( 2, CardSuite.HEART))
cl.append(Card( 2, CardSuite.SPADE))
cl.append(Card( 4, CardSuite.HEART))
cl.append(Card( 7, CardSuite.HEART))
cl.append(Card( 7, CardSuite.CLUB))

cl.append(Card( 9, CardSuite.CLUB))
cl.append(Card( 3, CardSuite.SPADE))
cl.append(Card(11, CardSuite.DIAMOND))
cl.append(Card( 7, CardSuite.SPADE))
cl.append(Card( 6, CardSuite.DIAMOND))
cl.append(Card( 8, CardSuite.CLUB))
cl.append(Card(12, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.DIAMOND))
cl.append(Card( 9, CardSuite.SPADE))
cl.append(Card( 1, CardSuite.CLUB))
cl.append(Card(12, CardSuite.DIAMOND))
cl.append(Card( 6, CardSuite.HEART))
cl.append(Card(13, CardSuite.SPADE))

cl.append(Card( 6, CardSuite.SPADE))
cl.append(Card(13, CardSuite.HEART))
cl.append(Card(11, CardSuite.SPADE))
cl.append(Card(13, CardSuite.DIAMOND))
cl.append(Card( 6, CardSuite.CLUB))
cl.append(Card(10, CardSuite.SPADE))
cl.append(Card( 5, CardSuite.SPADE))
cl.append(Card( 8, CardSuite.DIAMOND))
cl.append(Card( 5, CardSuite.HEART))
cl.append(Card( 5, CardSuite.CLUB))
cl.append(Card( 1, CardSuite.DIAMOND))
cl.append(Card(13, CardSuite.CLUB))
cl.append(Card( 2, CardSuite.CLUB))

cl.append(Card( 1, CardSuite.SPADE))
cl.append(Card(11, CardSuite.CLUB))
cl.append(Card( 8, CardSuite.HEART))
cl.append(Card( 4, CardSuite.SPADE))
cl.append(Card(11, CardSuite.HEART))
cl.append(Card(12, CardSuite.HEART))
cl.append(Card( 7, CardSuite.DIAMOND))
cl.append(Card( 2, CardSuite.DIAMOND))
cl.append(Card(10, CardSuite.DIAMOND))
cl.append(Card( 9, CardSuite.HEART))
cl.append(Card( 3, CardSuite.CLUB))
cl.append(Card( 3, CardSuite.DIAMOND))
cl.append(Card( 1, CardSuite.HEART))

s = Solution(cl)
sol = s.solve()
for i in sol:
    print(i)
