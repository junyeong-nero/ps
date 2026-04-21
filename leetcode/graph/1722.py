class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        
        if px > py: self.parent[px] = py
        else:       self.parent[py] = px
        return True
        

class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:

        n = len(source)

        d = DSU(n)
        for a, b in allowedSwaps:
            d.union(a, b)

        group = defaultdict(list)
        for i in range(n):
            p = d.find(i)
            group[p].append(i)

        res = 0
        # print(group)

        for group_id, group_list in group.items():
            c_src = Counter([source[index] for index in group_list])
            c_trg = Counter([target[index] for index in group_list])

            temp = 0
            for key in (c_src.keys() & c_trg.keys()):
                temp += min(c_src[key], c_trg[key])

            res += temp

        return n - res

        
