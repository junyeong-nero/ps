class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px < py:
            self.parent[py] = px
        else:
            self.parent[px] = py


class Solution:
    def numberOfComponents(self, properties: List[List[int]], k: int) -> int:
        n, m = len(properties), len(properties[0])
        properties = [Counter(row) for row in properties]

        def intersect(i, j):
            keys = properties[i].keys() & properties[j].keys()
            return len(keys)

        d = DSU(n)

        for i in range(n):
            for j in range(i):
                temp = intersect(i, j)
                if temp >= k:
                    d.union(i, j)

        temp = set()
        for i in range(n):
            temp.add(d.find(i))

        return len(temp)
