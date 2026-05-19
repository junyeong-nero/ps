class Solution:
    def lexSmallest(self, s: str) -> str:

        n = len(s)

        # select k in [1, n]
        # reverse first k chars, reverse last k chars

        # design:
        # - reverse operations: reverse(s[:k]) + reverse(s[k:])
        # - find lexicographically smallest string
        #    - reversed string starts with s[k]
        # all k should be s[k] = min(s)

        # time complexity
        # find k candidates : O(n)
        # reverse : O(n)

        res = s
        for k in range(n):
            temp1 = s[:k + 1][::-1] + s[k + 1:]
            temp2 = s[:k + 1] + s[k + 1:][::-1]

            res = min(res, temp1, temp2)
        
        return res
