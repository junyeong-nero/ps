class Solution:
    def mirrorDistance(self, n: int) -> int:
        
        def reverse(k):
            return int(str(k)[::-1])

        return abs(n - reverse(n))
