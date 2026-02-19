class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cons = [0, 0]
        i = 0
        n = len(s)
        res = 0

        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1

            cons[int(s[i])] = j - i
            res += min(cons)
            i = j

        return res
