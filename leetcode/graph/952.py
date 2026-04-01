import math
from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        while x != self.parent[x]:
            x = self.parent[x]
        return x

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False

        # 작은 트리를 큰 트리 밑으로
        if self.size[px] < self.size[py]:
            px, py = py, px

        self.parent[py] = px
        self.size[px] += self.size[py]
        return True


def prime_facto(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i

    if n > 1:
        factors.add(n)

    return factors


class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        d = defaultdict(set)
        p_nums = [(num, prime_facto(num)) for num in nums]

        for num, primes in p_nums:
            for prime in primes:
                d[prime].add(num)

        keys = sorted(d.keys())
        maps = {i: key for i, key in enumerate(keys)}
        maps_r = {key: i for i, key in enumerate(keys)}

        m = DSU(len(keys))

        for num, primes in p_nums:
            primes = list(primes)
            for i in range(len(primes) - 1):
                a, b = primes[i], primes[i + 1]
                i, j = maps_r[a], maps_r[b]
                m.union(i, j)

        # print(m.parent)

        z = defaultdict(set)
        for node in range(len(keys)):
            i = m.find(node)
            z[i] |= d[maps[node]]

        return max([len(v) for v in z.values()])
