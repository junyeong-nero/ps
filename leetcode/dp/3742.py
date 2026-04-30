from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        # dp[i][j][c]:
        # grid[i - 1][j - 1] 위치까지 cost c로 도달했을 때의 최대 score
        dp = [[[-1] * (k + 1) for _ in range(n + 1)] for _ in range(m + 1)]
        dp[1][1][0] = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                for cost_used in range(k + 1):
                    curr_score = dp[i][j][cost_used]

                    if curr_score == -1:
                        continue

                    # Move down
                    if i < m:
                        val = grid[i][j - 1]
                        extra_cost = 0 if val == 0 else 1
                        next_cost = cost_used + extra_cost

                        if next_cost <= k:
                            dp[i + 1][j][next_cost] = max(
                                dp[i + 1][j][next_cost],
                                curr_score + val
                            )

                    # Move right
                    if j < n:
                        val = grid[i - 1][j]
                        extra_cost = 0 if val == 0 else 1
                        next_cost = cost_used + extra_cost

                        if next_cost <= k:
                            dp[i][j + 1][next_cost] = max(
                                dp[i][j + 1][next_cost],
                                curr_score + val
                            )

        return max(dp[m][n])
