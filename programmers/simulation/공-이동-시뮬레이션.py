def solution(n, m, x, y, queries):
    r1 = r2 = x
    c1 = c2 = y

    for command, dist in reversed(queries):
        if command == 0:  # left
            # 역방향: right로 dist만큼 가능 범위 확장
            if c1 != 0:
                c1 += dist
            c2 = min(m - 1, c2 + dist)

        elif command == 1:  # right
            # 역방향: left로 dist만큼 가능 범위 확장
            if c2 != m - 1:
                c2 -= dist
            c1 = max(0, c1 - dist)

        elif command == 2:  # up
            # 역방향: down으로 dist만큼 가능 범위 확장
            if r1 != 0:
                r1 += dist
            r2 = min(n - 1, r2 + dist)

        elif command == 3:  # down
            # 역방향: up으로 dist만큼 가능 범위 확장
            if r2 != n - 1:
                r2 -= dist
            r1 = max(0, r1 - dist)

        # 범위가 완전히 격자 밖으로 밀리면 불가능
        if r1 >= n or r2 < 0 or c1 >= m or c2 < 0:
            return 0

        # 유효 범위로 보정
        r1 = max(0, r1)
        r2 = min(n - 1, r2)
        c1 = max(0, c1)
        c2 = min(m - 1, c2)

        if r1 > r2 or c1 > c2:
            return 0

    return (r2 - r1 + 1) * (c2 - c1 + 1)

# def solution(n, m, x, y, queries):
    
#     # 벽에 박았을 때, 움직임의 요소가 의미 없어짐.
#     # 생각을 해보자. (x, y) -> (x', y') 으로 가는데 벽에 박치기를 해서
#     # N번의 움직임이 상쇄되었다면, 도달하기 위한 경우의 수는... 
#     # (x + i, y), i in [0, N] 이렇게 된다.
    
#     dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    
#     def inbound(p, q):
#         return 0 <= p < n and 0 <= q < m
    
#     reached = set()
    
#     def dfs(x, y, query_index):
        
#         if query_index == -1:
#             nonlocal reached
#             reached.add((x, y))
#             return
        
#         command, dx = queries[query_index]
#         start = dx if inbound(x + dirs[command][0], y + dirs[command][1]) else 0
#         for i in range(start, dx + 1):
#             nx, ny = x - dirs[command][0] * i, y - dirs[command][1] * i
#             if not inbound(nx, ny):
#                 continue
#             dfs(nx, ny, query_index - 1)

#     dfs(x, y, len(queries) - 1)
#     return len(reached)
