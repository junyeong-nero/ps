from collections import deque

def solution(board):
    n = len(board)

    def empty(x, y):
        return 0 <= x < n and 0 <= y < n and board[x][y] == 0

    start = frozenset({(0, 0), (0, 1)})
    q = deque([(start, 0)])
    visited = {start}

    while q:
        robot, dist = q.popleft()

        if (n - 1, n - 1) in robot:
            return dist

        a, b = sorted(robot)

        # 평행이동
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            moved = frozenset({(a[0] + dx, a[1] + dy), (b[0] + dx, b[1] + dy)})
            if all(empty(x, y) for x, y in moved) and moved not in visited:
                visited.add(moved)
                q.append((moved, dist + 1))

        (x1, y1), (x2, y2) = a, b

        # 회전
        if x1 == x2:  # 가로
            for d in (-1, 1):  # 위, 아래
                if empty(x1 + d, y1) and empty(x2 + d, y2):
                    for pivot in ((x1, y1), (x2, y2)):
                        nxt = frozenset({pivot, (pivot[0] + d, pivot[1])})
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append((nxt, dist + 1))
        else:  # 세로
            for d in (-1, 1):  # 왼쪽, 오른쪽
                if empty(x1, y1 + d) and empty(x2, y2 + d):
                    for pivot in ((x1, y1), (x2, y2)):
                        nxt = frozenset({pivot, (pivot[0], pivot[1] + d)})
                        if nxt not in visited:
                            visited.add(nxt)
                            q.append((nxt, dist + 1))

    return -1
