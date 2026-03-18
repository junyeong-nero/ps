class Solution:
    def numberOfAlternatingGroups(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:

        n = len(colors)

        # O(n)
        def count_alter_groups(size):

            # color and position

            # d[0] = 0 in even position
            # d[1] = 0 in odd position

            d_red = [0, 0]
            d_blue = [0, 0]

            def check():
                # print(d_red, d_blue)

                if d_red[0] == 0 and d_blue[1] == 0 and d_red[1] + d_blue[0] == size:
                    return True
                if d_red[1] == 0 and d_blue[0] == 0 and d_red[0] + d_blue[1] == size:
                    return True
                return False

            for i in range(size):
                if colors[i] == 0:
                    d_red[i & 1] += 1
                if colors[i] == 1:
                    d_blue[i & 1] += 1

            res = 1 if check() else 0

            for i in range(n - 1):

                # shifting
                temp = (i + size) % n
                if colors[i] == 0:
                    d_red[0] -= 1
                if colors[i] == 1:
                    d_blue[0] -= 1

                d_red[0], d_red[1] = d_red[1], d_red[0]
                d_blue[0], d_blue[1] = d_blue[1], d_blue[0]

                if colors[temp] == 0:
                    d_red[(size - 1) & 1] += 1
                if colors[temp] == 1:
                    d_blue[(size - 1) & 1] += 1

                if check():
                    res += 1

            return res

        # O(1)
        def change(index, color):
            colors[index] = color
            return 0

        res = []

        # O(mn)
        for query in queries:
            if query[0] == 1:
                # print("=" * 10, query)
                res.append(count_alter_groups(query[1]))
            if query[0] == 2:
                change(query[1], query[2])

        return res


from sortedcontainers import SortedList


class Fenwick:

    def __init__(self, n: int):
        self.cnts = [0] * (n + 1)
        self.vals = [0] * (n + 1)

    def add(self, k: int, v: int) -> None:
        i = k + 1
        while i < len(self.cnts):
            self.cnts[i] += v
            self.vals[i] += k * v
            i += i & -i

    def query(self, k: int, v: int) -> int:
        ans = 0
        i = k + 1
        while i:
            ans += self.vals[i] - v * self.cnts[i]
            i -= i & -i
        return ans


class Solution:
    def numberOfAlternatingGroups(
        self, colors: List[int], queries: List[List[int]]
    ) -> List[int]:
        n = len(colors)
        i = 0
        mp = {}
        while i < n:
            for j in range(i, i + n):
                if colors[j % n] == colors[(j + 1) % n]:
                    break
            mp[j % n] = i
            i = j + 1
        groups = SortedList()
        fen = Fenwick(n + 1)

        dist = lambda i, j: j - i + 1 if i <= j else n + j - i + 1

        def add(i, j):
            groups.add((j, i))
            fen.add(dist(i, j), 1)

        def remove(k):
            j, i = groups.pop(k)
            fen.add(dist(i, j), -1)
            return i, j

        for j, i in mp.items():
            add(i, j)
        ans = []
        for q in queries:
            if q[0] == 1:
                if len(groups) == 1 and colors[groups[0][0]] != colors[groups[0][1]]:
                    val = n
                else:
                    _, sz = q
                    val = min(n, fen.query(n, sz - 1) - fen.query(sz - 1, sz - 1))
                ans.append(val)
            else:
                _, i, c = q
                if colors[i] != c:
                    colors[i] = c
                    k = groups.bisect_left((i, 0)) % len(groups)
                    lo, hi = remove(k)
                    if lo == i == hi:
                        if colors[(i - 1) % n] != colors[i]:
                            lo = remove((k - 1) % len(groups))[0]
                        if colors[i] != colors[(i + 1) % n] and groups:
                            hi = remove((k - 1) % len(groups) if k else 0)[1]
                        add(lo, hi)
                    elif lo == i != hi:
                        add((i + 1) % n, hi)
                        if colors[(i - 1) % n] != colors[i]:
                            lo = remove((k - 1) % len(groups))[0]
                        add(lo, i)
                    elif lo != i == hi:
                        add(lo, (i - 1) % n)
                        if colors[i] != colors[(i + 1) % n]:
                            hi = remove((k + 1) % len(groups) if i else 0)[1]
                        add(i, hi)
                    else:
                        i0 = (i - 1) % n
                        i1 = (i + 1) % n
                        if dist(lo, hi) == n and colors[lo] != colors[hi]:
                            add(i1, i0)
                        else:
                            add(lo, i0)
                            add(i1, hi)
                        add(i, i)
        return ans

