from typing import List

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7

        # dp[i][j] = [max_product, min_product]
        dp = [[[None, None] for _ in range(n)] for _ in range(m)]
        dp[0][0] = [grid[0][0], grid[0][0]]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue

                num = grid[i][j]
                candidates = []

                if i > 0:
                    candidates.append(dp[i - 1][j][0] * num)
                    candidates.append(dp[i - 1][j][1] * num)
                if j > 0:
                    candidates.append(dp[i][j - 1][0] * num)
                    candidates.append(dp[i][j - 1][1] * num)

                dp[i][j][0] = max(candidates)
                dp[i][j][1] = min(candidates)

        ans = dp[m - 1][n - 1][0]
        return ans % MOD if ans >= 0 else -1
