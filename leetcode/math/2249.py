from math import sqrt
from typing import List


class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:

        def get_lattice_points(circle):
            x, y, r = circle
            coords = set()
            for p in range(-r, r + 1):
                temp = int(sqrt(r**2 - abs(p) ** 2))
                for q in range(-temp, temp + 1):
                    coords.add((x + p, y + q))

            return coords

        res = set()
        for circle in circles:
            res |= get_lattice_points(circle)

        return len(res)
