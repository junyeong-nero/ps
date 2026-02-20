def solution(n, build_frame):
    # 현재 설치된 구조물들을 담을 집합 (x, y, a)
    structures = set()
    
    # 현재 구조물들이 모두 유효한지 검사하는 함수
    def check_valid(current_structures):
        for x, y, a in current_structures:
            if a == 0: # 기둥인 경우
                # 1. 바닥 위에 있거나
                # 2. 보의 한쪽 끝 부분 위에 있거나 (보는 (x-1, y) 또는 (x, y)에 존재)
                # 3. 다른 기둥 위에 있어야 함
                if y == 0 or \
                   (x - 1, y, 1) in current_structures or \
                   (x, y, 1) in current_structures or \
                   (x, y - 1, 0) in current_structures:
                    continue
                else:
                    return False
            else: # 보인 경우
                # 1. 한쪽 끝 부분이 기둥 위에 있거나 (기둥은 (x, y-1) 또는 (x+1, y-1)에 존재)
                # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 함
                if (x, y - 1, 0) in current_structures or \
                   (x + 1, y - 1, 0) in current_structures or \
                   ((x - 1, y, 1) in current_structures and (x + 1, y, 1) in current_structures):
                    continue
                else:
                    return False
        return True
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        
        if b == 1: # 설치
            structures.add(item)
            # 설치 후 모든 구조물이 규칙을 만족하는지 확인
            if not check_valid(structures):
                structures.remove(item) # 만족하지 않으면 취소
        else: # 삭제
            structures.remove(item)
            # 삭제 후 남은 구조물들이 규칙을 만족하는지 확인
            if not check_valid(structures):
                structures.add(item) # 만족하지 않으면 취소 (복구)
    
    # 정렬 조건: x좌표 오름차순, y좌표 오름차순, 기둥(0) 먼저
    answer = sorted(list(structures))
    
    # set의 요소는 튜플이므로 리스트로 변환하여 반환 (문제 요구사항은 2차원 배열)
    return [list(x) for x in answer]

# from collections import defaultdict, deque

# def solution(n, build_frame):
    
#     G = defaultdict(set)
#     G_r = defaultdict(set)
    
#     def is_connected(x, y):
#         if y == 0:
#             return True
        
#         for nx, ny in G_r[(x, y)]:
#             if is_connected(nx, ny):
#                 return True
#         return False
    
#     def is_leaf(x, y):
#         return len(G[(x, y)]) == 0
    
#     for x, y, a, b in build_frame:
#         # a : 0 -> 기둥 / 1 -> 보
#         # b : 0 -> 삭제 / 1 -> 설치
        
#         dx, dy = 0, 1
#         if a == 1:
#             dx, dy = 1, 0
        
#         if b == 1 and is_connected(x, y):
#             # 설치할 때 이 노드가 바닥과 연결되어 있는지 확인해야 함.
#             G[(x, y)].add((x + dx, y + dy))
#             G_r[(x + dx, y + dy)].add((x, y))
#         if b == 0 and is_leaf(x, y):
#             # 삭제할 때 이 노드의 child 노드가 없는지 확인해야 함.
#             parents = G_r[(x, y)]
#             for nx, ny in parents:
#                 G[(nx, ny)].remove(x, y)
#             G_r[(x, y)].clear()
        
#     def bfs(x, y):
#         q = deque([(x, y)])
#         visited = set()
#         while q:
#             cx, cy = q.popleft()
#             visited.add((cx, cy))
            
#             for nx, ny in G[(cx, cy)] | G_r[(cx, cy)]:
#                 if (nx, ny) in visited:
#                     continue
#                 q.append((nx, ny))
        
#         return visited
    
#     # print(G, G_r)
    
#     keys = G.keys()
#     for x, y in keys:
#         temp = bfs(x, y)
#         print(temp)
#         break
    
#     return []
    
#     # 5 <= n <= 100
#     # graph?
    
#     walls = set()
#     panes = set()
    
#     answer = [[]]
    
#     for x, y, a, b in build_frame:
        
#         target = walls if a == 0 else panes
#         if b == 0:
#             target.remove((x, y))
#         if b == 1:
#             target.add((x, y))
            
        
#         # a : 0 -> 기둥 / 1 -> 보
#         # b : 0 -> 삭제 / 1 -> 설치
#         # 보는 오른쪽, 기둥은 위로.
        
#     print(walls, panes)
#     walls = sorted(walls, key = lambda x: (x[1], x[0]))
    
#     visited = set()
    
#     def dfs(x, y):
#         if (x, y) in visited:
#             return
#         if (x, y) in walls:
#             visited.add((x, y, 0))
#             dfs(x, y + 1)
#         if (x, y) in panes:
#             visited.add((x, y, 1))
#             dfs(x + 1, y)
            
    
#     x, y = walls[0]
#     dfs(x, y)
#     print(visited)
    
#     return []
