class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        m, n = len(grid), len(grid[0])

        # rotate grid layer by layer
        # (0, 0) -> first layer
        #        (1, 1) -> second layer
        #               (2, 2) -> third layer

        board = [[0 for _ in range(n)] for _ in range(m)]

        def rotate_layer(level, k):
            a, b = m - level, n - level

            direction = 0
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            x, y = level, level
            arr = []

            # get layer elements
            while True:
                dx, dy = dirs[direction]
                nx, ny = x + dx, y + dy

                if nx < level or nx >= a or ny < level or ny >= b:
                    direction = (direction + 1) % 4
                    continue

                arr.append(grid[x][y])
                if nx == level and ny == level:
                    break
                x, y = nx, ny

            # rotate layer elements
            k %= len(arr)
            arr = arr[-k:] + arr[:-k]

            index = 0
            x, y = level, level

            # update rotated layer
            while True:
                dx, dy = dirs[direction]
                nx, ny = x + dx, y + dy

                if nx < level or nx >= a or ny < level or ny >= b:
                    direction = (direction + 1) % 4
                    continue

                board[x][y] = arr[index]
                if nx == level and ny == level:
                    break

                x, y = nx, ny
                index += 1

            return arr

        for level in range(min(m, n) // 2):
            rotate_layer(level, k)

        return board

