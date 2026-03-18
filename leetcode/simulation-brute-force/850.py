class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:

        MOD = 10**9 + 7

        events = defaultdict(dict)

        for x, y, x2, y2 in rectangles:
            events[y][x] = events[y].get(x, 0) + 1
            events[y][x2] = events[y].get(x2, 0) - 1

            events[y2][x] = events[y2].get(x, 0) - 1
            events[y2][x2] = events[y2].get(x2, 0) + 1

        # print(events)
        y_cands = sorted(events.keys())
        res = 0
        d = dict()

        for i, y in enumerate(y_cands):

            for x in events[y].keys():
                d[x] = d.get(x, 0) + events[y][x]

            cur = 0
            width = 0
            prev = 0
            for x in sorted(d.keys()):
                if cur > 0 and cur + d[x] <= 0:
                    width += x - prev
                    # width.append((prev, x))
                if cur <= 0 and cur + d[x] > 0:
                    prev = x
                cur += d[x]

            res += width * (y_cands[i + 1] - y) if i + 1 < len(y_cands) else 0
            res = res % MOD

            # print(y, d)
            # print(width)

        return res

