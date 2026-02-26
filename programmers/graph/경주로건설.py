import heapq

def solution(board):
    n = len(board)
    INF = 10**15
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # D, R, U, L

    # dist[x][y][dir] = (x,y)에 dir 방향으로 "도착"했을 때의 최소 비용
    dist = [[[INF] * 4 for _ in range(n)] for _ in range(n)]
    pq = []

    # 시작점: 방향이 정해져 있지 않으므로 4방향을 모두 시작 상태로 둔다
    for d in range(4):
        dist[0][0][d] = 0
        heapq.heappush(pq, (0, 0, 0, d))  # cost, x, y, dir

    while pq:
        cost, x, y, d = heapq.heappop(pq)
        if cost != dist[x][y][d]:
            continue

        for nd, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if board[nx][ny] == 1:
                continue

            add = 100 if nd == d else 600
            ncost = cost + add

            if ncost < dist[nx][ny][nd]:
                dist[nx][ny][nd] = ncost
                heapq.heappush(pq, (ncost, nx, ny, nd))

    return min(dist[n - 1][n - 1])

# def solution(board):
    
#     n = len(board)
#     dirs = [(1, 0),(0, 1),(-1, 0),(0, -1)]
    
#     visited = set()
#     def dfs(x, y, prev_dir, cost):
#         if x == n - 1 and y == n - 1:
#             return cost
#         res = float("inf")
        
#         visited.add((x, y))
#         for index, (dx, dy) in enumerate(dirs):
#             nx, ny = x + dx, y + dy
#             if nx < 0 or nx >= n or ny < 0 or ny >= n:
#                 continue
#             if (nx, ny) in visited:
#                 continue
#             if board[x][y] == 1:
#                 continue
#             new_cost = cost + (100 if prev_dir == -1 or prev_dir == index else 600)
#             res = min(res, dfs(nx, ny, index, new_cost))
            
#         visited.remove((x, y))
#         return res
    
#     answer = dfs(0, 0, -1, 0)
#     return answer
