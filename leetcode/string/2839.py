from collections import Counter

class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        even = Counter(s1[::2]) == Counter(s2[::2])
        odd = Counter(s1[1::2]) == Counter(s2[1::2])
        return even and odd
