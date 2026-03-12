from typing import List


class DSU:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if root_x < root_y:
            self.parent[root_y] = root_x
        else:
            self.parent[root_x] = root_y
        return True


class Solution:
    def maxStability(self, n: int, edges: List[List[int]], k: int) -> int:
        dsu = DSU(n)
        min_stability = float("inf")

        # 1) Add all mandatory edges first
        for u, v, strength, must in edges:
            if must != 1:
                continue

            # Mandatory edges must not create a cycle
            if not dsu.union(u, v):
                return -1

            min_stability = min(min_stability, strength)

        # 2) Add optional edges in descending order of strength
        selected_strengths = []
        edges.sort(key=lambda x: x[2], reverse=True)

        for u, v, strength, must in edges:
            if must == 1:
                continue

            if dsu.union(u, v):
                selected_strengths.append(strength)

        # 3) Check whether all nodes are connected
        roots = {dsu.find(i) for i in range(n)}
        if len(roots) != 1:
            return -1

        # 4) Double the weakest selected edges up to k times
        selected_strengths.sort()
        for i in range(min(len(selected_strengths), k)):
            selected_strengths[i] *= 2

        if selected_strengths:
            min_stability = min(min_stability, min(selected_strengths))

        return -1 if min_stability == float("inf") else min_stability
