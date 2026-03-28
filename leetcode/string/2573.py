
class DSU:

    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px > py:
            self.parent[px] = py
        else:
            self.parent[py] = px


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)

        # [[4,0,2,0],
        #  [0,3,0,1],
        #  [2,0,2,0],
        #  [0,1,0,1]]

        # [[4,3,2,1],
        #  [3,3,2,1],
        #  [2,2,2,1],
        #  [1,1,1,3]]

        # lcp[0][3] = 2 => LCP("abab", "ab")
        # lcp[1][4] = 1 => LCP("bab", "b")


        ### Union-Find

        for i in range(n):
            if lcp[i][i] != n - i:
                return ""
            for j in range(i, n):
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > min(n - i, n - j):
                    return ""

        d = DSU(n)

        for i in range(n):
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    d.union(i, j)
        
        used = dict()
        delta = 0
        res = []

        for i in range(n):
            p = d.find(i)
            if p not in used:
                if delta >= 26:
                    return ""
                used[p] = chr(ord("a") + delta)
                delta += 1

            res.append(used[p])

        s = "".join(res)

        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = 0

        for i in range(n):
            for j in range(n):
                if dp[i][j] != lcp[i][j]:
                    return ""

        return s


        ### Naive Approach

        for i in range(n):
            for j in range(i, n):
                if i == j and lcp[i][j] != n - i:
                    return ""
                if lcp[i][j] != lcp[j][i]:
                    return ""
                if lcp[i][j] > min(n - i, n - j):
                    return ""


        res = [-1] * n
        index = 0

        for i in range(n):
            
            if res[i] == -1:
                res[i] = index
                index += 1

            for j in range(i + 1, n):
                cur = lcp[i][j]
                if cur == 0:
                    if res[j] == -1:
                        res[j] = index 
                        index += 1
                    if res[j] == res[j - 1]:
                        return ""
                else:
                    for k in range(cur):
                        res[j + k] = res[i + k]
        
        # print(res)
        res = "".join([chr(ord("a") + elem) for elem in res])
        return res
