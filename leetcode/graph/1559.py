class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:

        visited, visited_cur = set(), set()
        stack = deque()

        row_n = len(grid)
        col_n = len(grid[0])

        for row, row_g in enumerate(grid):
            for col, val in enumerate(row_g):
                if (row, col) not in visited:  # if new cell

                    # add to stack current cell and previous cell
                    # we don't have previous cell, so replace it to -1, -1
                    stack.append([row, col, -1, -1])
                    visited_cur.clear()
                    while stack:

                        r, c, r_prv, c_prv = stack.pop()
                        if (r, c) in visited_cur:
                            return True  # we saw this cell before -> cycle
                        visited_cur.add((r, c))

                        for d_r, d_c in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                            # we exclude previous cell from addition to stack
                            if (
                                0 <= r + d_r < row_n
                                and (r + d_r, c + d_c) != (r_prv, c_prv)
                                and 0 <= c + d_c < col_n
                                and grid[r + d_r][c + d_c] == val
                            ):
                                stack.append([r + d_r, c + d_c, r, c])

                    visited.update(visited_cur)  # add current set to general set

        return False

