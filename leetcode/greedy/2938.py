class Solution:
    def minimumSteps(self, s: str) -> int:
        
        n = len(s)
        count = 0
        res = 0
        
        for i in range(n):
            if s[i] == "1":
                count += 1
            else:
                res += count
        
        return res
