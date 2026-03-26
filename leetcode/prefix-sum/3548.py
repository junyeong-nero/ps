from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        total = 0

        # Frequency arrays
        bottom = [0] * 100001
        top =[0] * 100001
        left = [0] * 100001
        right = [0] * 100001

        # Initialize
        for row in grid:
            for x in row:
                total += x
                bottom[x] += 1
                right[x] += 1

        sum_top = 0

        # 🔹 Horizontal cuts
        for i in range(m - 1):
            for j in range(n):
                val = grid[i][j]
                sum_top += val

                top[val] += 1
                bottom[val] -= 1

            sum_bottom = total - sum_top

            if sum_top == sum_bottom:
                return True

            diff = abs(sum_top - sum_bottom)

            if diff <= 100000:
                if sum_top > sum_bottom:
                    if self.check(top, grid, 0, i, 0, n - 1, diff):
                        return True
                else:
                    if self.check(bottom, grid, i + 1, m - 1, 0, n - 1, diff):
                        return True

        sum_left = 0

        # 🔹 Vertical cuts
        for j in range(n - 1):
            for i in range(m):
                val = grid[i][j]
                sum_left += val

                left[val] += 1
                right[val] -= 1

            sum_right = total - sum_left

            if sum_left == sum_right:
                return True

            diff = abs(sum_left - sum_right)

            if diff <= 100000:
                if sum_left > sum_right:
                    if self.check(left, grid, 0, m - 1, 0, j, diff):
                        return True
                else:
                    if self.check(right, grid, 0, m - 1, j + 1, n - 1, diff):
                        return True

        return False

    def check(self, freq: List[int], grid: List[List[int]], r1: int, r2: int, c1: int, c2: int, diff: int) -> bool:
        rows = r2 - r1 + 1
        cols = c2 - c1 + 1

        # Single cell
        if rows * cols == 1:
            return False

        # 1D row
        if rows == 1:
            return grid[r1][c1] == diff or grid[r1][c2] == diff

        # 1D column
        if cols == 1:
            return grid[r1][c1] == diff or grid[r2][c1] == diff

        # 2D case
        return freq[diff] > 0

    def _alternative_dp_approach(self, grid: List[List[int]]) -> bool:
        """
        [Brainstorming Notes / 이전 접근 방식]
        
        어제 풀었던 문제와 다른점?
        1개의 셀을 없앨 수 있다. 근데 이게 이전 영역에서 없어지는지, 혹은 다른 영역에서 없어지는지 모름.
        이전 영역에서 없어진다고 하면 어느정도 트래킹이 가능하긴하다.
        -> 한쪽만 커버하게 하고, 양방향으로 DP 를 쓰면 될 것 같다.

        트래킹을 어떻게 할것인가? DP 에 state 를 하나 더 추가하자.
        dp[i][j][0], dp[i][j][1] 이렇게.
        0 은 하나도 안지운거, 1 은 하나를 지운거 이렇게!! -> 나 개천재인듯
        근데 1이 되면 어디에서 지운건지 모르는데. ...

        A : area of current
        B : area of other side
        B = total - A
        check A - elem in A == B
         => check A - B == elem in A
        """
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp_visited = [[{0} for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (
                    grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
                )
                dp_visited[i][j] = (
                    dp_visited[i - 1][j] | dp_visited[i][j - 1] | {grid[i - 1][j - 1]}
                )

                if j == n or i == m:
                    A = dp[i][j]
                    B = total - A
                    diff = A - B

                    if diff == 0:
                        return True

                    if j == 1:
                        if grid[0][j - 1] == diff or grid[m - 1][j - 1] == diff:
                            return True
                    elif i == 1:
                        if grid[i - 1][0] == diff or grid[i - 1][n - 1] == diff:
                            return True
                    elif diff in dp_visited[i][j]:
                        return True

        # Re-initialize for reverse traversal
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        dp_visited = [[{0} for _ in range(n + 1)] for _ in range(m + 1)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[i][j] = grid[i][j] + dp[i + 1][j] + dp[i][j + 1] - dp[i + 1][j + 1]
                dp_visited[i][j] = (
                    dp_visited[i + 1][j] | dp_visited[i][j + 1] | {grid[i][j]}
                )

                if j == 0 or i == 0:
                    A = dp[i][j]
                    B = total - A
                    diff = A - B
                    
                    if diff == 0:
                        return True

                    if j == n - 1:
                        if grid[0][j] == diff or grid[m - 1][j] == diff:
                            return True
                    elif i == m - 1:
                        if grid[i][0] == diff or grid[i][n - 1] == diff:
                            return True
                    elif diff in dp_visited[i][j]:
                        return True

        return False
