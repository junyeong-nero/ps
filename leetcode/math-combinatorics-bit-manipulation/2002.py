class Solution:
    def maxProduct(self, s: str) -> int:

        ### Bit Mask ### 
        
        n = len(s)
        pal_len = [0] * (1 << n)

        # 1) 전처리: 각 mask의 부분수열이 팰린드롬이면 길이 저장
        for mask in range(1, 1 << n):
            seq = []
            for i in range(n):
                if mask & (1 << i):
                    seq.append(s[i])
            # 팰린드롬 체크
            if seq == seq[::-1]:
                pal_len[mask] = len(seq)

        # 2) 팰린드롬 mask들 중 서로 disjoint인 쌍 최대
        ans = 0
        for a in range(1, 1 << n):
            if pal_len[a] == 0:
                continue
            for b in range(1, 1 << n):
                if (a & b) == 0 and pal_len[b] > 0:
                    ans = max(ans, pal_len[a] * pal_len[b])

        return ans


        ### DFS solution ### 

        # n = len(s)
        # def is_palindrome(s):
        #     return s == s[::-1]

        # @cache
        # def dfs(cur, s1, s2):
        #     if cur == n:
        #         if is_palindrome(s1) and is_palindrome(s2):
        #             return len(s1) * len(s2)
        #         return float("-inf")

        #     res = float("-inf")    
        #     res = max(res, dfs(cur + 1, s1, s2))
        #     res = max(res, dfs(cur + 1, s1 + s[cur], s2))
        #     res = max(res, dfs(cur + 1, s1, s2 + s[cur]))
        #     return res
        
        # res = dfs(0, "", "")
        # return res
            
            
        
