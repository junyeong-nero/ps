class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if k == 1:
            return [[0 for _ in range(n)] for _ in range(m)]

        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):

                temp = []

                for x in range(i, i + k):
                    for y in range(j, j + k):
                        temp.append(grid[x][y])

                if k == 1:
                    ans[i][j] = 0
                    continue

                temp = sorted(set(temp))

                if len(temp) <= 1:
                    ans[i][j] = 0
                    continue

                mini = float('inf')
                for p in range(1, len(temp)):
                    mini = min(mini, abs(temp[p] - temp[p - 1]))

                ans[i][j] = mini

        return ans
        

        ### My Solution

        def func(s):
            arr = sorted(s)
            res = float("inf")
            for i in range(len(arr) - 1):
                res = min(res, arr[i + 1] - arr[i])
            
            return res

        dp = [[Counter() for _ in range(n + 1 - k)] for _ in range(m + 1 - k)]
        res = [[0 for _ in range(n + 1 - k)] for _ in range(m + 1 - k)]

        for row in grid[:k]:
            dp[0][0] += Counter(row[:k])

        res[0][0] = func(dp[0][0].keys())

        for i in range(m + 1 - k):
            for j in range(n + 1 - k):
                
                if i == 0 and j == 0:
                    continue

                if i - 1 >= 0:
                    dp[i][j] += dp[i - 1][j]
                    dp[i][j] -= Counter(grid[i - 1][j:j + k])
                    
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j - 1]
                    dp[i][j] -= Counter([row[j - 1] for row in grid[i:i + k]])

                dp[i][j][grid[i + k - 1][j + k - 1]] += 1
                
                res[i][j] = func(dp[i][j].keys())
                
        print(dp)
        return res

