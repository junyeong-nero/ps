class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        
        if len(s) != len(goal):
            return False

        n = len(s)

        for i in range(n):
            shifted = s[i:] + s[:i]
            if shifted == goal:
                return True
        
        return False
