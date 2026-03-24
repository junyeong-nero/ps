class Solution:
    def beautifulPartitions(self, s: str, k: int, minLength: int) -> int:
        MOD = 10**9 + 7
        primes = set("2357")
        n = len(s)

        ### DP

        if s[0] not in primes or s[-1] in primes:
            return 0

        # valid boundary start
        can_start = [0] * n
        for i in range(n):
            if s[i] in primes and (i == 0 or s[i - 1] not in primes):
                can_start[i] = 1

        # dp_prev[i] = s[:i]를 c-1개로 나누는 경우의 수
        dp_prev = [0] * (n + 1)
        dp_prev[0] = 1

        for part in range(1, k + 1):
            dp_cur = [0] * (n + 1)
            prefix = 0

            for i in range(1, n + 1):
                start_idx = i - minLength
                if start_idx >= 0 and can_start[start_idx]:
                    prefix = (prefix + dp_prev[start_idx]) % MOD

                # 마지막 조각이 i에서 끝날 수 있으려면 s[i-1]가 non-prime
                if s[i - 1] not in primes:
                    dp_cur[i] = prefix

            dp_prev = dp_cur

        return dp_prev[n]


        ### DFS + memoization

        @cache
        def dfs(index, count = 0):
            if index == n:
                return 1 if count == k else 0
            if s[index] not in primes:
                return 0

            j = index + 1
            res = 0
            while j < n:
                length = j - index + 1
                if s[j] not in primes:
                    if minLength <= length <= maxLength:
                        res += dfs(j + 1, count + 1)
                j += 1

            return res % MOD

        res = dfs(0)
        return res

        # 3312958
        # 331 | 29 | 58
