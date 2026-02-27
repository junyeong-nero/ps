from typing import List


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for x in range(1, m + 1):
            for y in range(1, n + 1):
                dp[x][y] = (
                    dp[x - 1][y] + dp[x][y - 1] - dp[x - 1][y - 1] + grid[x - 1][y - 1]
                )

        def area(x, y):
            temp = dp[x][y] - dp[x - 3][y] - dp[x][y - 3] + dp[x - 3][y - 3]
            temp -= grid[x - 2][y - 3] + grid[x - 2][y - 1]
            return temp

        res = 0
        for i in range(3, m + 1):
            for j in range(3, n + 1):
                temp = area(i, j)
                res = max(res, temp)

        return res
