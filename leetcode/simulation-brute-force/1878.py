class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])

        def func(x, y, size):
            if x + 2 * size >= m or y + size >= n or y - size < 0:
                return float("-inf")
            res = grid[x][y]
            if size == 0:
                return res

            # size = 1
            for dx in range(1, 2 * size):
                nx = x + dx
                # print(
                #     grid[nx][y - (dx if dx <= size else size - dx)],
                #     grid[nx][y + (dx if dx <= size else size - dx)],
                # )
                res += grid[nx][y + (dx if dx <= size else 2 * size - dx)]
                res += grid[nx][y - (dx if dx <= size else 2 * size - dx)]

            res += grid[x + size * 2][y]
            return res

        d = set()

        for i in range(m):
            for j in range(n):
                max_size = min((m - 1 - i) // 2, j, n - 1 - j)
                for size in range(max_size + 1):
                    temp = func(i, j, size)
                    if temp > 0:
                        d.add(temp)

        return sorted(d, reverse=True)[:3]

