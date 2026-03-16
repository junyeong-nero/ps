class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                if s[i] != s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]
                else:
                    left = i + 1
                    right = j - 1

                    while left <= right and s[left] != s[i]:
                        left += 1
                    while left <= right and s[right] != s[i]:
                        right -= 1

                    if left > right:
                        # 안쪽에 같은 문자가 없음
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 2
                    elif left == right:
                        # 안쪽에 같은 문자가 1개 있음
                        dp[i][j] = dp[i + 1][j - 1] * 2 + 1
                    else:
                        # 안쪽에 같은 문자가 2개 이상 있음
                        dp[i][j] = dp[i + 1][j - 1] * 2 - dp[left + 1][right - 1]

                dp[i][j] %= MOD

        return dp[0][n - 1]

# class Solution:
#     def countPalindromicSubsequences(self, s: str) -> int:
#         # number of non-empty palindromic subsequences
#         MOD = 10 ** 9 + 7
#         n = len(s)

#         # palindrome -> abcd 밖에 사용 안함.
#         # DP 사용할 수 있을 것 같다.
#         # bi-directional 하게 할 수는 없을까?

#         # stack 을 이용해볼까.?
#         # 새로운 문자가 들어왔을 때 stack[-1] 과 같으면 pop 해버리는 접근이 되게 좋아보인다.

#         def ispalindrome(s):
#             return s == s[::-1]

#         visited = set()
#         visited.add("")

#         for i in range(n):

#             new_visited = set()
#             for key in visited:
        
#                 new_visited.add(key)
#                 new_visited.add(key + s[i])

#             visited = new_visited
                
#         visited.remove("")
#         res = sum([1 for key in visited if ispalindrome(key)])
#         return res
