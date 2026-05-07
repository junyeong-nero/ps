from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time_ahead = 0

        for p, s in cars:
            time = (target - p) / s

            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time

        return fleets

# class DSU:

#     def __init__(self, n):
#         self.parent = list(range(n))
    
#     def find(self, x):
#         if x != self.parent[x]:
#             self.parent[x] = self.find(self.parent[x])
#         return self.parent[x]

#     def union(self, x, y):
#         px, py = self.find(x), self.find(y)
#         if px == py:
#             return True
#         if px < py:
#             self.parent[py] = px
#         if px > py:
#             self.parent[px] = py
#         return False


# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
#         # start mile 0 -> target

#         # 1. check is_fleet with two cars
#         # 2. union-find with fleet cars
#         # 3. return # of groups

#         # design:
#         # n = 10^5 -> solve in O(n log n)
#         # is_fleet -> O(1)
#         # union-find -> O(log n)
#         # iterate all cars (n^2)

#         n = len(position)

#         def is_fleet(i, j):
#             x, y = position[i], position[j]
#             vx, vy = speed[i], speed[j]

#             if vx == vy:
#                 return x == y

#             t = (x - y) / (vy - vx)
#             return max(x, y) <= x + vx * t <= target

#         d = DSU(n)

#         for i in range(n):
#             for j in range(i):
#                 print(i, j, is_fleet(i, j))
#                 if is_fleet(i, j):
#                     d.union(i, j)

#         res = set()
#         for i in range(n):
#             res.add(d.find(i))

#         return len(res)
