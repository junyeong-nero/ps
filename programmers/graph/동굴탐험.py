from collections import defaultdict, deque

def solution(n, path, order):
    graph = defaultdict(list)
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    # prerequisite[b] = a  => b를 가기 전에 a를 먼저 방문해야 함
    prerequisite = {}
    for a, b in order:
        prerequisite[b] = a

    # 시작점 0이 잠겨 있으면 불가능
    if 0 in prerequisite:
        return False

    visited = [False] * n
    waiting = {}      # prerequisite가 아직 안 풀려서 대기 중인 노드
    unlock = {}       # 어떤 노드를 방문하면 열리는 노드

    for a, b in order:
        unlock[a] = b

    q = deque([0])
    visited[0] = True
    count = 1

    while q:
        cur = q.popleft()

        # cur를 방문해서 열리는 노드가 있으면 처리
        if cur in unlock:
            nxt = unlock[cur]
            if nxt in waiting:
                q.append(nxt)
                visited[nxt] = True
                count += 1
                del waiting[nxt]

        for nxt in graph[cur]:
            if visited[nxt]:
                continue

            # 선행 방문이 필요한데 아직 그 선행 노드를 방문하지 못했으면 대기
            if nxt in prerequisite and not visited[prerequisite[nxt]]:
                waiting[nxt] = True
                continue

            visited[nxt] = True
            count += 1
            q.append(nxt)

    return count == n

# from collections import defaultdict

# def solution(n, path, order):
    
#     graph = defaultdict(list)
#     for u, v in path:
#         graph[u].append(v)
#         graph[v].append(u)
    
#     # a, b 로 이어지는 루트가 contradiction 인지 확인
#     # 4 -> 1 : 4 7 0 1 (무조건 7을 먼저 지나감)
#     # 8 -> 7 : 8 1 0 7 (무조건 1을 먼저 지나감)
#     # 6 -> 5 : 6 3 0 7 5 (무조건 7을 먼저 지나감)
    
#     visited = set()
    
#     def route(start, end):
#         if start == end:
#             return [end]
    
#         visited.add(start)
#         for node in graph[start]:
#             if node in visited:
#                 continue
#             temp = route(node, end)
#             if temp:
#                 return [start] + temp
#         visited.remove(start)
#         return []
    
#     def check_route(r):
#         r = "".join([str(c) for c in r])
#         for start, end in order:
#             left = r.find(str(start))
#             right = r.find(str(end))
            
#             if left >= 0 and right >= 0 and left > right:
#                 return False
#             if left < 0 and right >= 0:
#                 return False
            
#         return True
            
#     for start, end in order:
#         visited.clear()
#         r = route(start, end)
#         # print(r)
#         if check_route(r):
#             return True
    
#     return False
