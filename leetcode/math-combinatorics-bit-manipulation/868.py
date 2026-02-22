class Solution:
    def binaryGap(self, n: int) -> int:
        index = 0
        prev = 100
        res = 0
        while (1 << index) < n:
            num = n & (1 << index)
            if num:
                res = max(res, index - prev)
                prev = index
            index += 1
        
        return resclass Solution:
    def binaryGap(self, n: int) -> int:
        index = 0
        prev = 100
        res = 0
        while (1 << index) < n:
            num = n & (1 << index)
            if num:
                res = max(res, index - prev)
                prev = index
            index += 1
        
        return res
