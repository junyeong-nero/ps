class Solution:
    def eatenApples(self, apples: List[int], expire: List[int]) -> int:

        n = len(apples)
        q = []
        day = 0
        res = 0

        while q or day < n:
            if day < n:
                heappush(q, [day + expire[day], apples[day]])
            while q and (q[0][0] <= day or q[0][1] == 0):
                heappop(q)
            if q:
                q[0][1] -= 1
                res += 1
            day += 1

        return res

