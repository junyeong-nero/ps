class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum([sum(row) for row in grid])
        if total & 1:
            return False

        area = [[0 for i in range(n + 1)] for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                area[i][j] = (
                    grid[i - 1][j - 1]
                    + area[i - 1][j]
                    + area[i][j - 1]
                    - area[i - 1][j - 1]
                )
                if i == m and area[i][j] == total // 2:
                    return True
                if j == n and area[i][j] == total // 2:
                    return True

        return False

