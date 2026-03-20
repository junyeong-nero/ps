class Solution:
    def countKConstraintSubstrings(
        self, S: str, k: int, Q: List[List[int]]
    ) -> List[int]:
        l, n = 0, len(S)
        cnt, L, ans = [0, 0], [], []

        for r in range(n):
            cnt[int(S[r])] += 1
            while l < r and min(cnt) > k:
                cnt[int(S[l])] -= 1
                l += 1
            L.append(l)

        V = [r - L[r] + 1 for r in range(n)]
        P = list(accumulate(V, initial=0))
        for li, ri in Q:
            k = bisect_left(L, li, lo=li, hi=ri + 1)
            lft = k - li
            c1 = (1 + lft) * lft // 2
            c2 = P[ri + 1] - P[k]
            ans.append(c1 + c2)

        return ans

        n = len(s)

        # all substrings : 7 + 6 + 5 + 4 + 3 + 2 + 1 = 28
        # 28 - 2 excepts two cases

        # f(s, 0) : s 에서 0의 개수
        # f(s, 0) <= k or f(s, 1) = n - f(s, 0) <= k

        ### DP

        # dp[i] = number k-constraint substrings in: s[0:i - 1]
        # dp[i + 1] = dp[i] + (i + 1) 를 포함한 k-constraint substring 의 개수

        dp = [0] * (n + 1)

        for i in range(1, n + 1):

            temp = 0
            d = [0, 0]

            for j in range(i - 1, -1, -1):
                d[int(s[j])] += 1
                if d[0] > k and d[1] > k:
                    break
                temp += 1

            dp[i] = dp[i - 1] + temp

        print(dp)

        res = []
        for l, r in queries:
            print(dp[r + 1], dp[l])
            res.append(dp[r + 1] - dp[l])

        return res

