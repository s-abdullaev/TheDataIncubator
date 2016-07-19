from __future__ import division
import numpy as np

class Knight(object):
    def __init__(self):
        self.curpos=0
        self.moves = []
        self.validmoves={
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [3, 9, 0],
            5: [],
            6: [1, 7, 0],
            7: [2, 6],
            8: [1, 3],
            9: [4, 2]
        }
        
    def move(self):
        m=np.random.choice(self.validmoves[self.curpos])
        self.moves.append(m)
        self.curpos=m
        return m
    
    def multimove(self, steps):
        for _ in range(steps): self.move()
    
    def getSum(self, modulo=0):
        return np.sum(self.moves) % modulo if modulo else np.sum(self.moves)
    
if __name__=="__main__":
    T = 1024
    modulo=1024
    tests = 10000

    np.random.seed(123)

    Q1sols=[]
    for _ in range(tests):
        k=Knight()
        k.multimove(T)
        Q1sols.append(k.getSum())

    print '%.8f, %.8f' % (np.mean(Q1sols), np.std(Q1sols))
    
    #conditional probability
    countA=sum(1 for x in Q1sols if x % 29 == 0)
    countAnB=sum(1 for x in Q1sols if x % 23 == 0 and x % 29 == 0)
    
    print '%d, %d, %.10f' % (countA, countAnB, countAnB/countA)
    