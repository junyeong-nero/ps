class DSU:
    def __init__(self):
        self.parent = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[py] = px


class Solution:
    def gcdSort(self, nums: List[int]) -> bool:

        # nums[i] -> 를 target 자리로 옮겨야 됨.
        # gcd > 0 인 그룹끼리 자리를 바꿀 수 있음. -> 소인수분해?
        # 3, 2*3, 3*5

        d = DSU()
        def get_prime_factors(x):
            factors = set()
            d = 2
            while d * d <= x:
                if x % d == 0:
                    factors.add(d)
                    while x % d == 0:
                        x //= d
                d += 1
            if x > 1:
                factors.add(x)
            return factors

        factor_to_num = {}

        for x in nums:
            factors = get_prime_factors(x)
            for f in factors:
                if f in factor_to_num:
                    d.union(x, factor_to_num[f])
                else:
                    factor_to_num[f] = x

        sorted_nums = sorted(nums)
        for a, b in zip(nums, sorted_nums):
            if d.find(a) != d.find(b):
                return False

        return True

        n = len(nums)

        ### Union-Find Approach

        target = sorted(nums)
        p = list(set(nums))
        m = len(p)
        d = d(nums)

        # bottleneck O(N^2)
        for i in range(m):
            for j in range(i):
                if gcd(p[i], p[j]) > 1:
                    d.union(p[i], p[j])

        for i in range(n):
            if d.find(target[i]) != d.find(nums[i]):
                return False

        return True

