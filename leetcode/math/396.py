class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        temp = 0
        index = n - 1
        for i, v in enumerate(nums):
            temp += i * v

        res = -math.inf
        for i in range(n):
            res = max(res, temp)
            temp += total
            temp -= n * nums[index]
            index -= 1

        return res
