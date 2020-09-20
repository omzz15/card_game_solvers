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
        
    
cl = list()
cl.append(Card(12, CardSuite.HEART))
cl.append(Card( 6, CardSuite.SPADE))
cl.append(Card( 9, CardSuite.DIAMOND))
cl.append(Card( 1, CardSuite.DIAMOND))
cl.append(Card( 9, CardSuite.SPADE))
cl.append(Card(13, CardSuite.CLUB))
cl.append(Card( 1, CardSuite.HEART))
cl.append(Card(13, CardSuite.SPADE))
cl.append(Card( 7, CardSuite.SPADE))
cl.append(Card( 3, CardSuite.SPADE))
cl.append(Card( 2, CardSuite.SPADE))
cl.append(Card( 9, CardSuite.HEART))
cl.append(Card( 4, CardSuite.HEART))

cl.append(Card( 3, CardSuite.DIAMOND))
cl.append(Card( 8, CardSuite.HEART))
cl.append(Card( 5, CardSuite.HEART))
cl.append(Card( 8, CardSuite.DIAMOND))
cl.append(Card(11, CardSuite.SPADE))
cl.append(Card(10, CardSuite.HEART))
cl.append(Card(11, CardSuite.DIAMOND))
cl.append(Card( 7, CardSuite.CLUB))
cl.append(Card(10, CardSuite.DIAMOND))
cl.append(Card( 7, CardSuite.DIAMOND))
cl.append(Card( 1, CardSuite.SPADE))
cl.append(Card(12, CardSuite.SPADE))
cl.append(Card(13, CardSuite.DIAMOND))

cl.append(Card( 8, CardSuite.SPADE))
cl.append(Card(11, CardSuite.CLUB))
cl.append(Card( 3, CardSuite.CLUB))
cl.append(Card( 1, CardSuite.CLUB))
cl.append(Card(11, CardSuite.HEART))
cl.append(Card( 9, CardSuite.CLUB))
cl.append(Card( 6, CardSuite.HEART))
cl.append(Card( 8, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.DIAMOND))
cl.append(Card( 2, CardSuite.HEART))
cl.append(Card( 3, CardSuite.HEART))
cl.append(Card( 7, CardSuite.HEART))
cl.append(Card( 2, CardSuite.DIAMOND))

cl.append(Card(12, CardSuite.DIAMOND))
cl.append(Card( 2, CardSuite.CLUB))
cl.append(Card( 4, CardSuite.DIAMOND))
cl.append(Card( 4, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.SPADE))
cl.append(Card( 6, CardSuite.DIAMOND))
cl.append(Card( 4, CardSuite.SPADE))
cl.append(Card( 6, CardSuite.CLUB))
cl.append(Card(10, CardSuite.CLUB))
cl.append(Card(12, CardSuite.CLUB))
cl.append(Card( 5, CardSuite.CLUB))
cl.append(Card(10, CardSuite.SPADE))
cl.append(Card(13, CardSuite.HEART))

Card.validate_deck(cl)
s = Solution(cl)
sol = s.solve()
for i in sol:
    print(i)