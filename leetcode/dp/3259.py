from typing import List


class Solution:
    def maxEnergyBoost(self, a: List[int], b: List[int]) -> int:
        n = len(a)
        
        dp = [[0, 0], [0, 0]]
        # dp[i][j] = maximum energy with 
        for i in range(n):
            p, q = dp[0][0], dp[0][1]

            dp[0][0] = max(dp[0][0] + a[i], dp[1][1] + a[i])
            dp[0][1] = max(dp[0][1] + b[i], dp[1][0] + b[i])
            dp[1][0], dp[1][1] = p, q

        # print(dp)
        return max(dp[0])
