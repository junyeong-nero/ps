class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        even, odd = [0, 0], [0, 0]
        for i in range(n):
            if i & 1:
                odd[int(s[i])] += 1
            else:
                even[int(s[i])] += 1

        res = min(n - even[0] - odd[1], n - even[1] - odd[0])
        return res
