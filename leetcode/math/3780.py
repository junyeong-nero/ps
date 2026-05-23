class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        
        nums = sorted(nums, reverse=True)

        d = [[], [], []]
        for num in nums:
            d[num % 3].append(num)

        # 0 0 0
        # 1 1 1
        # 0 1 2
        # 2 2 2

        res = 0
        if len(d[0]) >= 3:
            res = max(res, sum(d[0][:3]))
        if len(d[1]) >= 3:
            res = max(res, sum(d[1][:3]))
        if len(d[2]) >= 3:
            res = max(res, sum(d[2][:3]))
        if d[0] and d[1] and d[2]:
            res = max(res, d[0][0] + d[1][0] + d[2][0])

        return res
