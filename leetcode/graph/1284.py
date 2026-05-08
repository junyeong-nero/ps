class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        # flip: choose one cell -> flip it, with 4 neighbors

        m, n = len(mat), len(mat[0])

        def convert(mat):
            res = 0
            for i in range(m):
                for j in range(n):
                    index = i * n + j
                    if mat[i][j] == 1:
                        res |= 1 << index
            return res

        def flip(cur, x, y):
            dirs = [1, 0, -1, 0, 1]
            cur ^= 1 << x * n + y

            for i in range(4):
                nx = x + dirs[i]
                ny = y + dirs[i + 1]
                if nx >= m or nx < 0 or ny >= n or ny < 0:
                    continue
                index = nx * n + ny
                cur ^= 1 << index

            return cur

        mat = convert(mat)

        visited = dict()
        visited[mat] = 0

        q = deque([(mat, 0)])

        while q:

            cur, dist = q.popleft()
            if cur == 0:
                return dist
            # visited[cur] = dist

            for i in range(m):
                for j in range(n):

                    new = flip(cur, i, j)
                    new_dist = dist + 1

                    if new_dist < visited.get(new, float("inf")):
                        visited[new] = new_dist
                        q.append((new, new_dist))

        return -1

