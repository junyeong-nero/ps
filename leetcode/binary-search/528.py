import random
from bisect import bisect_right
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        
        prefix = [0]
        for num in w:
            prefix.append(prefix[-1] + num)
        self.weights = prefix


    def pickIndex(self) -> int:
        t = random.randint(0, self.weights[-1] - 1)
        index = bisect_right(self.weights, t) - 1
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
