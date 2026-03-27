from typing import List

class Solution:
    def longestCommonSubpath(self, n: int, paths: List[List[int]]) -> int:
        paths.sort(key=len)
        mod1 = 1_000_000_007
        mod2 = 1_000_000_009
        base = 100_000_19

        def check(length: int) -> bool:
            if length == 0:
                return True

            common = None

            for path in paths:
                if len(path) < length:
                    return False

                seen = set()

                h1 = 0
                h2 = 0
                power1 = 1
                power2 = 1

                for _ in range(length):
                    power1 = (power1 * base) % mod1
                    power2 = (power2 * base) % mod2

                for i, x in enumerate(path):
                    val = x + 1  # 0 때문에 구분 안 되는 상황 방지

                    h1 = (h1 * base + val) % mod1
                    h2 = (h2 * base + val) % mod2

                    if i >= length:
                        old = path[i - length] + 1
                        h1 = (h1 - old * power1) % mod1
                        h2 = (h2 - old * power2) % mod2

                    if i >= length - 1:
                        seen.add((h1, h2))

                if common is None:
                    common = seen
                else:
                    common &= seen

                if not common:
                    return False

            return True

        left, right = 0, len(paths[0])
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans

        ### LCS extension with DP
        # MLE

        # LCS 느낌으로 풀어야 할 것 같은데, DP 사용해야됨
        # 그런데 여러 paths 에 대해서 수행해야되는데. 어떻게 할지?

        def LCS(paths):

            lengths = [len(path) for path in paths]
            dp = dict()

            res = 0
            for pos in product(*[range(1, elem + 1) for elem in lengths]):
                if len(set([paths[i][j - 1] for i, j in enumerate(pos)])) == 1:
                    neg_pos = tuple([elem - 1 for elem in pos])
                    dp[pos] = dp.get(neg_pos, 0) + 1
                    res = max(res, dp[pos])
                else:
                    dp[pos] = 0

            return res

        temp = LCS(paths)
        print(temp)

        return temp

        ### trie approach?
        # 중복 도시 방문을 해결하지 못함.

        maps = [[0] * (n + 1) for _ in range(n + 1)]
        # maps[u][v] = u -> v counting

        for path in paths:
            for i in range(len(path) - 1):
                u, v = path[i], path[i + 1]
                maps[u][v] += 1
            maps[path[-1]][n] += 1

        # print(maps)

        start_points = [node for node in range(n) if sum(maps[node]) == m]
        # print(start_points)

        def traverse(cur):
            res = 1
            for node, count in enumerate(maps[cur]):
                if count != m:
                    continue
                res = max(res, 1 + traverse(node))

            return res

        if not start_points:
            return 0

        res = 0
        for point in start_points:
            temp = traverse(point)
            # print(point, temp)
            res = max(res, temp)

        return res

