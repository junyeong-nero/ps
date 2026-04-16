class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        n = len(nums)
        d = defaultdict(set)
        for i, num in enumerate(nums):
            d[num].add(i)

        # print(d)

        res = []
        for query in queries:
            temp = n
            
            for j in d[nums[query]]:
                if query == j:
                    continue
                temp = min(temp, abs(query - j), n - abs(query - j))

            res.append(temp if temp < n else -1)

        return res

    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries
