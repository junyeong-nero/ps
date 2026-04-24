class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # swapping, end state : [123, 450]
        # board size fixed [2, 3]
        # 2 * 3

        # bit-mask dp?
        # convert board state to bitwise.
        # let index
        # [0, 1, 2]
        # [3, 4, 5]

        dirs = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4],
        }

        # [4, 1, 2]
        # [5, 0, 3]

        # 0 -> 4
        # 1 -> 1
        # 2 -> 2
        # 3 -> 5
        # 4 -> 0
        # 5 -> 3
        # answer = 305214

        def convert(board):
            pos = [0] * 6
            for i in range(2):
                for j in range(3):
                    cur = board[i][j]
                    pos[cur] = i * 3 + j

            return pos

        target = convert([[1, 2, 3], [4, 5, 0]])

        q = deque([convert(board)])
        visited = set()
        level = 0

        while q:

            for _ in range(len(q)):

                cur = q.popleft()
                if tuple(cur) in visited:
                    continue
                if cur == target:
                    return level

                visited.add(tuple(cur))
                for node in range(6):
                    if cur[node] not in dirs[cur[0]]:
                        continue
                    cur[0], cur[node] = cur[node], cur[0]
                    if tuple(cur) not in visited:
                        q.append(cur[:])
                    cur[0], cur[node] = cur[node], cur[0]

            level += 1

        return -1

