from collections import deque
from typing import List

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def in_range(x, y):
            return 0 <= x < m and 0 <= y < n

        def is_wall(x, y):
            return not in_range(x, y) or grid[x][y] == '#'

        # 시작 위치 찾기
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'S':
                    player = (i, j)
                elif grid[i][j] == 'B':
                    box = (i, j)
                elif grid[i][j] == 'T':
                    target = (i, j)

        def can_reach(start, goal, box_pos):
            """
            플레이어가 현재 box를 통과하지 않고 goal까지 걸어갈 수 있는지 확인
            """
            if start == goal:
                return True

            q = deque([start])
            visited = {start}

            while q:
                x, y = q.popleft()

                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy

                    if not in_range(nx, ny):
                        continue
                    if (nx, ny) in visited:
                        continue
                    if grid[nx][ny] == '#':
                        continue
                    if (nx, ny) == box_pos:
                        continue

                    if (nx, ny) == goal:
                        return True

                    visited.add((nx, ny))
                    q.append((nx, ny))

            return False

        # state = (box_x, box_y, player_x, player_y)
        q = deque([(box[0], box[1], player[0], player[1], 0)])
        visited = {(box[0], box[1], player[0], player[1])}

        while q:
            bx, by, px, py, pushes = q.popleft()

            if (bx, by) == target:
                return pushes

            for dx, dy in dirs:
                nbx, nby = bx + dx, by + dy          # 박스가 밀려갈 위치
                req_px, req_py = bx - dx, by - dy    # 플레이어가 밀기 위해 서 있어야 할 위치

                # 박스가 이동할 칸이 벽이면 안 됨
                if is_wall(nbx, nby):
                    continue

                # 플레이어가 서야 하는 칸도 유효해야 함
                if is_wall(req_px, req_py):
                    continue

                # 현재 플레이어 위치에서 req_p까지 box를 통과하지 않고 갈 수 있어야 함
                if not can_reach((px, py), (req_px, req_py), (bx, by)):
                    continue

                # 박스를 밀면 플레이어는 기존 박스 위치로 이동
                npx, npy = bx, by
                state = (nbx, nby, npx, npy)

                if state in visited:
                    continue

                visited.add(state)
                q.append((nbx, nby, npx, npy, pushes + 1))

        return -1

# from collections import deque
# from typing import List

# class Solution:
#     def minPushBox(self, grid: List[List[str]]) -> int:
#         m, n = len(grid), len(grid[0])

#         def inbound(pos):
#             x, y = pos
#             return 0 <= x < m and 0 <= y < n

#         def get_block(pos):
#             if not inbound(pos):
#                 return "#"
#             return grid[pos[0]][pos[1]]

#         dirs = [
#             (0, 1),
#             (-1, 0),
#             (0, -1),
#             (1, 0),
#         ]

#         def get_move_pos(pos, index):
#             return (pos[0] + dirs[index % 4][0], pos[1] + dirs[index % 4][1])

#         end_pos = None
#         box_pos = None
#         player_pos = None

#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == "T":
#                     end_pos = (i, j)
#                 elif grid[i][j] == "S":
#                     player_pos = (i, j)
#                 elif grid[i][j] == "B":
#                     box_pos = (i, j)

#         def get_reachable(cur_player_pos):
#             reachable = set()
#             q = deque([cur_player_pos])

#             while q:
#                 tar = q.popleft()
#                 if tar in reachable:
#                     continue
#                 reachable.add(tar)

#                 for i in range(4):
#                     new_pos = get_move_pos(tar, i)
#                     if new_pos in reachable:
#                         continue
#                     if get_block(new_pos) != "B" and get_block(new_pos) != "#":
#                         q.append(new_pos)

#             return reachable

#         def pushable_actions(cur_box_pos, cur_player_pos):
#             arr = []
#             reachable = get_reachable(cur_player_pos)

#             for i in range(4):
#                 move_pos = get_move_pos(cur_box_pos, i)      # 박스가 이동할 칸
#                 push_pos = get_move_pos(cur_box_pos, i + 2)  # 플레이어가 밀기 위해 있어야 할 칸

#                 if get_block(move_pos) != "#" and get_block(push_pos) != "#" and push_pos in reachable:
#                     arr.append(i)

#             return arr

#         visited = set()

#         def dfs(cur_box_pos, cur_player_pos):
#             if cur_box_pos == end_pos:
#                 return 0

#             state = (cur_box_pos, cur_player_pos)
#             if state in visited:
#                 return float("inf")
#             visited.add(state)

#             res = float("inf")
#             actions = pushable_actions(cur_box_pos, cur_player_pos)

#             for action in actions:
#                 new_box_pos = get_move_pos(cur_box_pos, action)
#                 new_player_pos = cur_box_pos  # 박스를 밀면 플레이어는 기존 박스 위치로 이동

#                 grid[cur_box_pos[0]][cur_box_pos[1]] = "."
#                 grid[new_box_pos[0]][new_box_pos[1]] = "B"

#                 res = min(res, 1 + dfs(new_box_pos, new_player_pos))

#                 grid[new_box_pos[0]][new_box_pos[1]] = "."
#                 grid[cur_box_pos[0]][cur_box_pos[1]] = "B"

#             visited.remove(state)
#             return res

#         res = dfs(box_pos, player_pos)
#         return -1 if res == float("inf") else res


# # ["#",".",".","#","T","#","#","#","#"],
# # ["#",".",".","#",".","#",".",".","#"],
# # ["#",".",".","#",".","#","B",".","#"],
# # ["#",".",".",".",".",".",".",".","#"],
# # ["#",".",".",".",".","#",".","S","#"],
# # ["#",".",".","#",".","#","#","#","#"]
