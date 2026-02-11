class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.pos = defaultdict(list)
        for i, val in enumerate(arr):
            self.pos[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        if value not in self.pos:
            return 0

        indices = self.pos[value]
        l = bisect.bisect_left(indices, left)
        r = bisect.bisect_right(indices, right)
        return r - l

        
# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
