class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        n = len(s)
        i = 0
        while i < n and s[i] == "1":
            i += 1

        while i < n:
            if s[i] == "1":
                return False
            i += 1

        return True
            
