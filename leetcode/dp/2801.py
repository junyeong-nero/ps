class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:

        MOD = 10 ** 9 + 7
        
        # stepping numbers
        # abs diff = 1 for adj digits
        # DP style ?

        # counting all steps is exploding
        # int high < 10^100 
        # at each digit -> 10
        # 10^1000? no.

        # tracking only ends digit.
        # then how we can harness boundary ?
        # prefix approach -! 
        # prefix[high] - prefix[low] 

        # handling upper bound is quite tricky.
        # cannot chech the exact number 

        n = len(high)
        dp = [[0] * 10 for _ in range(n + 1)]
        for i in range(10):
            dp[0][i] = 1

        # dp[i] = number of endswith i (include 0)

        for i in range(1, n + 1):

            for j in range(10):
                if j + 1 < 10: dp[i][j + 1] += dp[i - 1][j]
                if j - 1 >= 0: dp[i][j - 1] += dp[i - 1][j]

        
        print(dp)
    
        def func(num):
            m = len(num)
            res = sum(dp[m - 1][1:int(num[0]) + 1])

            for i in range(1, m):
                print(res)
                pos = m - i - 1
                res += sum(dp[pos][:int(num[i]) + 1]) - sum(dp[pos][int(num[i]) + 1:])
            
            return res

        print(low, func(low))
        print(high, func(high))

        return 0


from functools import lru_cache

class Solution:
    def countSteppingNumbers(self, low: str, high: str) -> int:
        MOD = 10**9 + 7

        def minus_one(s: str) -> str:
            return str(int(s) - 1)

        def count_leq(num: str) -> int:
            # 0 이하 처리
            if num == "0":
                return 0

            n = len(num)

            @lru_cache(None)
            def dfs(pos: int, prev: int, tight: int, started: int) -> int:
                if pos == n:
                    return 1 if started else 0

                limit = int(num[pos]) if tight else 9
                ans = 0

                for d in range(limit + 1):
                    ntight = 1 if (tight and d == limit) else 0

                    if not started:
                        if d == 0:
                            # 아직 숫자 시작 안 함
                            ans += dfs(pos + 1, 0, ntight, 0)
                        else:
                            # 새로 시작
                            ans += dfs(pos + 1, d, ntight, 1)
                    else:
                        if abs(d - prev) == 1:
                            ans += dfs(pos + 1, d, ntight, 1)

                return ans % MOD

            return dfs(0, 0, 1, 0)

        low_minus_one = minus_one(low)
        ans = (count_leq(high) - count_leq(low_minus_one)) % MOD
        return ans
