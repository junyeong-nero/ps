class DSU:
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        self.parent[py] = px


class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[bool]:

        dsu = DSU(n)

        for i in range(1, n):
            if nums[i] - nums[i - 1] <= maxDiff:
                dsu.union(i - 1, i)

        return [dsu.find(u) == dsu.find(v) for u, v in queries]
