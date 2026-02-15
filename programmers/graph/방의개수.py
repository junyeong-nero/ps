def solution(arrows):
    # 0~7 방향: (dx, dy)
    dirs = {
        0: (0, 1),
        1: (1, 1),
        2: (1, 0),
        3: (1, -1),
        4: (0, -1),
        5: (-1, -1),
        6: (-1, 0),
        7: (-1, 1),
    }

    visited_nodes = set()
    visited_edges = set()  # 간선은 (a,b) 방향 모두 저장(무방향)

    x, y = 0, 0
    visited_nodes.add((x, y))
    rooms = 0

    for d in arrows:
        dx, dy = dirs[d]

        # 대각선 교차 처리를 위해 "한 칸 이동"을 2번으로 쪼갬
        # (좌표를 2배로 확장한 효과)
        for _ in range(2):
            nx, ny = x + dx, y + dy

            edge = ((x, y), (nx, ny))
            redge = ((nx, ny), (x, y))

            # 이미 방문한 정점으로 "처음 보는 간선"으로 들어가면 방 1개 생성
            if (nx, ny) in visited_nodes and edge not in visited_edges:
                rooms += 1

            visited_nodes.add((nx, ny))
            visited_edges.add(edge)
            visited_edges.add(redge)

            x, y = nx, ny

    return rooms

