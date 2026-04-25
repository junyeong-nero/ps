from typing import List
from collections import deque
from dataclasses import dataclass


@dataclass
class Sequence:
    startX: int
    startY: int
    endX: int
    endY: int
    length: int


class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        ordered = self.getOrderedPoints(side, points)

        def dist(a, b, c, d):
            return abs(a - c) + abs(b - d)

        def check(d: int) -> bool:
            dq = deque()
            dq.append(Sequence(
                ordered[0][0], ordered[0][1],
                ordered[0][0], ordered[0][1],
                1
            ))

            max_len = 1

            for i in range(1, len(ordered)):
                x, y = ordered[i]

                startX, startY = x, y
                length = 1

                while dq and dist(x, y, dq[0].endX, dq[0].endY) >= d:
                    seq = dq.popleft()

                    if dist(x, y, seq.startX, seq.startY) >= d and seq.length + 1 >= length:
                        startX = seq.startX
                        startY = seq.startY
                        length = seq.length + 1
                        max_len = max(max_len, length)

                dq.append(Sequence(startX, startY, x, y, length))

            return max_len >= k

        left, right = 0, side

        while left < right:
            mid = (left + right + 1) // 2

            if check(mid):
                left = mid
            else:
                right = mid - 1

        return left

    def getOrderedPoints(self, side: int, points: List[List[int]]) -> List[List[int]]:
        left = []
        top = []
        right = []
        bottom = []

        for x, y in points:
            if x == 0 and y > 0:
                left.append([x, y])
            elif y == side and x > 0:
                top.append([x, y])
            elif x == side and y < side:
                right.append([x, y])
            else:
                bottom.append([x, y])

        left.sort(key=lambda p: p[1])
        top.sort(key=lambda p: p[0])
        right.sort(key=lambda p: -p[1])
        bottom.sort(key=lambda p: -p[0])

        return left + top + right + bottom
