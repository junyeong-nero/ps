from collections import deque


def solution(grid):
    N = len(grid)
    M = len(grid[0])
    group = [[[0] * 2 for _ in range(M)] for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 현재 삼각형이 |\, |/, \|, /| 일 때 이동 가능 방향
    dir_map = [
        [1, 2],
        [0, 2],
        [0, 3],
        [1, 3]
    ]
    # 현재 삼각형이 |\, |/, \|, /| 일 때 위/아래 삼각형의 state
    updown_state = [
        [1, 0],
        [0, 1],
        [0, 1],
        [1, 0]
    ]

    def is_valid(x, y):
        return 0 <= x < N and 0 <= y < M

    def bfs(x, y, state, group_num):
        q = deque()
        q.append((x, y, state))
        group[x][y][state] = group_num

        size = 0
        while q:
            cx, cy, cstate = q.popleft()
            size += 1

            # 현재 삼각형 모양
            # 0 : |\, 1 : |/, 2 : \|, 3 : /|
            if grid[cx][cy] == -1:
                shape = 0 if cstate == 0 else 2
            else:
                shape = 1 if cstate == 0 else 3

            for i in range(2):
                nd = dir_map[shape][i]
                nx = cx + dx[nd]
                ny = cy + dy[nd]

                if not is_valid(nx, ny):
                    continue
                if group[nx][ny][0] == group_num or group[nx][ny][1] == group_num:
                    continue

                # 다음 삼각형의 state 결정
                if nd == 0 or nd == 1:
                    nstate = updown_state[shape][0 if grid[nx][ny] == -1 else 1]
                else:
                    nstate = 1 if nd == 2 else 0  # 왼쪽이면 1, 오른쪽이면 0

                group[nx][ny][nstate] = group_num
                q.append((nx, ny, nstate))

        return size

    answer = 0
    group_num = 1

    for i in range(N):
        for j in range(M):
            for k in range(2):
                if group[i][j][k] == 0:
                    answer = max(answer, bfs(i, j, k, group_num))
                    group_num += 1

    return answer
