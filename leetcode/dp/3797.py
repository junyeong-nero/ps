from math import sqrt
from typing import List

class Solution:
    def numberOfRoutes(self, grid: List[str], d: int) -> int:
        n, m = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # dp[i][j][0]: 아래쪽 행에서 (i, j)로 도착한 경우의 수
        # dp[i][j][1]: 같은 행에서 (i, j)로 이동한 경우의 수
        dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

        # Base case: 맨 아래 행 초기화
        for j in range(m):
            if grid[n - 1][j] != "#":
                dp[n - 1][j][0] = 1

        # 수직 이동 시 허용되는 가로 거리 (피타고라스 정리: x^2 + 1^2 <= d^2 -> x <= sqrt(d^2-1))
        # d=1이면 window_size=0이 되어야 함
        window_size = int(sqrt(d**2 - 1)) if d > 1 else 0

        # 아래 행부터 위로 올라가며 계산
        for i in range(n - 1, -1, -1):
            
            # 1. 아래 행(i+1)에서 현재 행(i)으로 오는 경우 (State 0 갱신)
            if i + 1 < n:
                # i+1행의 (State 0 + State 1)에 대한 누적 합 계산
                prefix_sum = [0] * (m + 1)
                for k in range(m):
                    val = (dp[i + 1][k][0] + dp[i + 1][k][1]) % MOD
                    prefix_sum[k + 1] = (prefix_sum[k] + val) % MOD
                
                for j in range(m):
                    if grid[i][j] == "#":
                        continue
                    
                    # 범위: [j - window_size, j + window_size]
                    left = max(0, j - window_size)
                    right = min(m - 1, j + window_size)
                    
                    # 구간 합 계산 (O(1))
                    count = (prefix_sum[right + 1] - prefix_sum[left]) % MOD
                    dp[i][j][0] = count

            # 2. 같은 행(i) 내에서 이동하는 경우 (State 1 갱신)
            # 현재 행의 State 0에 대한 누적 합 계산 (이미 위에서 State 0이 채워졌음)
            prefix_sum_curr = [0] * (m + 1)
            for k in range(m):
                val = dp[i][k][0]
                prefix_sum_curr[k + 1] = (prefix_sum_curr[k] + val) % MOD
            
            for j in range(m):
                if grid[i][j] == "#":
                    continue
                
                # 범위: [j - d, j + d]
                left = max(0, j - d)
                right = min(m - 1, j + d)
                
                # 구간 합 계산
                count = (prefix_sum_curr[right + 1] - prefix_sum_curr[left]) % MOD
                
                # 주의: 같은 위치(j)에서 제자리 이동하는 경우는 제외해야 함
                # (문제 조건 혹은 로직상 '이동'이 발생해야 하므로)
                self_val = dp[i][j][0]
                count = (count - self_val + MOD) % MOD
                
                dp[i][j][1] = count

        # 맨 윗줄(0번 행)의 모든 경우의 수 합산
        res = 0
        for j in range(m):
            res = (res + dp[0][j][0] + dp[0][j][1]) % MOD
            
        return res

# class Solution:
#     def numberOfRoutes(self, grid: List[str], d: int) -> int:
#         n, m = len(grid), len(grid[0])
#         # row n - 1 to 0
#         # available to available
#         # movable distance <= d
#         # move rows or stay
#         # stay only one turn.

#         # use DP

#         # dp[i][j][k]
#         # i: row index
#         # j: column index
#         # k: left in rows (if 1, go to up rows.)

#         window_size = int(sqrt(d**2 - 1))

#         # from below row
#         # dp[i][j][0] += dp[i + 1][j - window_size][0] + ... + dp[i - 1][j + window_size][0]
#         # dp[i][j][0] += dp[i + 1][j - window_size][1] + ... + dp[i - 1][j + window_size][1]

#         # from current row
#         # dp[i][j][1] += dp[i][j - d][0] + ... + dp[i][j + d][0]

#         MOD = 10**9 + 7
#         dp = [[[0, 0] for _ in range(m)] for _ in range(n)]

#         # start from bottom row
#         for j in range(m):
#             if grid[n - 1][j] != "#":
#                 dp[n - 1][j][0] = 1

#         for i in range(n - 1, -1, -1):
#             if 0 <= i + 1 < n:
#                 for j in range(m):
#                     if grid[i][j] == "#":
#                         continue
#                     dp[i][j][0] += sum(
#                         [
#                             dp[i + 1][x][0] + dp[i + 1][x][1]
#                             for x in range(
#                                 max(0, j - window_size), min(m, j + window_size + 1)
#                             )
#                             if grid[i + 1][x] != "#"
#                         ]
#                     )
#                     dp[i][j][0] %= MOD

#             for j in range(m):
#                 if grid[i][j] == "#":
#                     continue
#                 dp[i][j][1] += sum(
#                     [
#                         dp[i][x][0]
#                         for x in range(max(0, j - d), min(m, j + d + 1))
#                         if grid[i][x] != "#" and x != j
#                     ]
#                 )
#                 dp[i][j][1] %= MOD

#         # print(dp)
#         res = sum([dp[0][j][0] + dp[0][j][1] for j in range(m)])
#         return res % MOD

