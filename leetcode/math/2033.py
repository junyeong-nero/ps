class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m, n = len(grid), len(grid[0])
        arr = []

        target = grid[0][0] % x
        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != target:
                    return -1
                arr.append((grid[i][j] - target) // x)

        arr.sort()
        mid = arr[len(arr) // 2]
        
        res = 0
        for num in arr:
            res += abs(num - mid)

        return res
        



