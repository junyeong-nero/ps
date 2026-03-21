class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        
        for i in range(k // 2):
            a, b = x + i, x + k - 1 - i
            for j in range(y, y + k):
                grid[a][j], grid[b][j] = grid[b][j], grid[a][j]

        return grid
