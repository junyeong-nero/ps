class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        
        nums = sorted(nums)
        n = len(nums)
        res = float("inf")
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            res = min(res, b - a)

        return res
