# Mathematical Approach

class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 1 or sum > 9 * num:
            return ""

        q, r = divmod(sum, 9)
        zeros = num - q - (1 if r > 0 else 0)
        if zeros < 0:
            return ""

        ans = []
        if q > 0:
            ans.append('9' * q)
        if r > 0:
            ans.append(str(r))
        if zeros > 0:
            ans.append('0' * zeros)
        return ''.join(ans)
    

# DFS + DP solution

class Solution:
    def maxSumOfSquares(self, a: int, b: int) -> str:
        # dp[i][j]: i번째 자리까지 사용했을 때, 합이 j인 경우의 최대 제곱합
        # parent[i][j]: 그때 선택한 숫자 (역추적용)
        dp = [[-1] * (b + 1) for _ in range(a + 1)]
        parent = [[-1] * (b + 1) for _ in range(a + 1)]
        
        dp[0][0] = 0
        
        for i in range(a):
            for j in range(b + 1):
                if dp[i][j] == -1:
                    continue
                
                # 첫 번째 자리는 0이 올 수 없음 (a > 1인 경우 상정)
                start = 1 if i == 0 else 0
                # 남은 자릿수(a-i-1)로 채울 수 있는 최대 합은 (a-i-1) * 9
                # 따라서 현재 선택할 숫자 k는 j + k + (남은 최대합) >= b 여야 함
                for k in range(start, 10):
                    if j + k <= b:
                        new_score = dp[i][j] + k**2
                        if new_score >= dp[i + 1][j + k]:
                            dp[i + 1][j + k] = new_score
                            parent[i + 1][j + k] = k

        # 만약 목표 합 b를 만들 수 없다면 빈 문자열 반환
        if dp[a][b] == -1:
            return ""

        # 역추적 (Backtracking)
        res = []
        curr_b = b
        for i in range(a, 0, -1):
            digit = parent[i][curr_b]
            res.append(str(digit))
            curr_b -= digit
            
        return "".join(res[::-1])

# class Solution:
#     def maxSumOfSquares(self, a: int, b: int) -> str:

#         memo = dict()

#         def dfs(digit, value):
#             if (digit, value) in memo:
#                 return memo[(digit, value)]
            
#             if digit == a:
#                 if value > 0:
#                     return float("-inf"), ""
#                 return 0, ""
            
#             res, res_char = float("-inf"), ""
#             start = 1 if digit == 0 else 0
#             for i in range(min(value, 9), start - 1, -1):
#                 score, char = dfs(digit + 1, value - i)
#                 if score + i ** 2 > res:
#                     res = score + i ** 2
#                     res_char = str(i) + char

#             memo[(digit, value)] = (res, res_char)
#             return res, res_char

#         score, char = dfs(0, b)
#         return char
