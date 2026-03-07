import sys
sys.setrecursionlimit(1000000)

class DSU:
    
    def __init__(self):
        self.d = dict()
        
    def up(self, x):
        if x not in self.d:
            self.d[x] = x + 1
            return x
        if x != self.d[x]:
            self.d[x] = self.up(self.d[x])
        return self.d[x]

def solution(k, room_number):
    
    d = DSU()
    res = []
    for num in room_number:
        res.append(d.up(num))
    
    return res
