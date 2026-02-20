class Solution:
    def longestPalindromicSubsequence(self, s: str, k: int) -> int:

        def diff(a, b):
            a, b = min(a, b), max(a, b)
            return min(ord(b) - ord(a), ord(a) + 26 - ord(b))
        
        @cache
        def dfs(left, right, remain=k):

            if left < 0 or right >= n:
                return 0

            res = 0
            res = max(res, dfs(left - 1, right, remain))
            res = max(res, dfs(left, right + 1, remain))

            if (d := diff(s[left], s[right])) <= remain:
                res = max(res, (1 if left == right else 2) + dfs(left - 1, right + 1, remain - d))
            
            return res

        n = len(s)
        res = 1
        for i in range(1, n):
            res = max(res, dfs(i - 1, i))
            res = max(res, dfs(i, i))

        return res
