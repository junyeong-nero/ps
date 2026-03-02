from collections import defaultdict
from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:

        events = defaultdict(list)
        events_r = defaultdict(list)
        for x, y, a, b in rectangles:
            events[y].append((x, a))
            events_r[b].append((x, a))

        def concat(arr):
            arr = sorted(arr)
            res = []
            i = 0
            while i < len(arr):
                j = i
                while j + 1 < len(arr) and arr[j][1] == arr[j + 1][0]:
                    j += 1
                res.append((arr[i][0], arr[j][1]))
                i = j + 1
            return res

        def check(column):
            A = concat(events[column])
            B = concat(events_r[column])
            return A == B

        columns = sorted(events.keys() | events_r.keys())
        if len(concat(events[columns[0]])) > 1:
            return False
        if len(concat(events_r[columns[-1]])) > 1:
            return False

        for column in columns[1:-1]:
            if not check(column):
                return False

        return True
