class Solution:
    def minCost(self, n: int, cost: List[List[int]]) -> int:
        # dp[i][j][k]: 
        # The minimum cost to paint both ends from 0 to i and from n - 1 to n - 1 - i. 
        # The i-th house is painted color j.
        # The (n - 1 - i)-th house is painted color k.
        dp = [
            [[float("inf") for k in range(3)] for j in range(3)] for i in range(n // 2)
        ]

        # Paint from both ends toward middle.
        for i in range(n // 2):

            # Enumerate all possible color combinations
            for j in range(3):
                for k in range(3):
                    
                    # Equidistant houses from the ends should have different color.
                    if j == k:
                        continue

                    dp[i][j][k] = cost[i][j] + cost[n - 1 - i][k]
                    if i != 0:
                        # Enumerate all possible color combination of previous pair,
                        # but adjacent houses should have different color.
                        dp[i][j][k] += min(
                            dp[i - 1][l][m]
                            for l in range(3)
                            for m in range(3)
                            if l != m and l != j and m != k
                        )

        return min(min(v) for v in dp[n // 2 - 1])
