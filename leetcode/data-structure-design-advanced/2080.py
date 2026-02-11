from bisect import bisect_left, bisect_right
from collections import defaultdict
from typing import List


class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, val in enumerate(arr):
            self.pos[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0

        indices = self.pos[value]
        left_idx = bisect_left(indices, left)
        right_idx = bisect_right(indices, right)
        return right_idx - left_idx

        
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
