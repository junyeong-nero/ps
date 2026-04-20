class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        # dp[i] : index 까지 걸리는 maximum_steps
        # dp[0] = 0

        n = len(nums)
        dp = [-float("inf")] * n
        dp[0] = 0
        
        for j in range(1, n):
            for i in range(j):
                if -target <= nums[j] - nums[i] <= target:
                    dp[j] = max(dp[j], dp[i] + 1)
        
        return dp[-1] if dp[-1] > 0 else -1
