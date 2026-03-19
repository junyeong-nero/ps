class Solution:
    def lexicographicallySmallestString(self, S: str) -> str:
        N = len(S)
        A = [ord(c) - ord("a") for c in S]

        @cache
        def empty(i, j):
            # Can S[i..j] be removed completely?
            if i > j:
                return 1
            if abs(A[i] - A[j]) in [1, 25] and empty(i + 1, j - 1):
                return 1
            return any(empty(i, k) and empty(k + 1, j) for k in range(i + 1, j, 2))

        @cache
        def dp(i):
            # Answer for S[i:]
            if i == N:
                return ""
            ans = S[i] + dp(i + 1)
            for j in range(i + 1, N, 2):
                if empty(i, j):
                    ans = min(ans, dp(j + 1))
            return ans

        return dp(0)

        ### DFS

        # remove any pair of adjacent chars
        # n = 250 -> O(n^3)
        n = len(s)

        def is_adj(a, b):
            if abs(ord(a) - ord(b)) == 1:
                return True
            if (a == "a" and b == "z") or (a == "z" and b == "a"):
                return True
            return False

        # 오랜만에 DFS
        # n 범위가 너무 길어서 bitmask 는 못쓸 것 같고 ..
        # 아니면 stack or queue 이런거 써야될 것 같은데..

        removed = [False] * n

        def get_next(i):
            j = i + 1
            while j < n and removed[j]:
                j += 1
            return j

        def get_prev(i):
            j = i - 1
            while j >= 0 and removed[j]:
                j -= 1
            return j

        def check_removals():

            arr = []
            for i in range(1, n):
                if removed[i]:
                    continue

                prev = get_prev(i)
                if prev == -1:
                    continue

                if is_adj(s[prev], s[i]):
                    arr.append((prev, i))

            return arr

        res = s

        def dfs():
            nonlocal res
            cur = [s[i] for i in range(n) if not removed[i]]
            cur = "".join(cur)

            # print(cur)
            res = min(res, cur)

            removals = check_removals()
            for i, j in removals:
                removed[i], removed[j] = True, True
                dfs()
                removed[i], removed[j] = False, False

        dfs()
        return res

