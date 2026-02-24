import heapq
from collections import defaultdict, deque

def solution(n, roads, sources, destination):
    
    graph = defaultdict(list)
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
        
    visited = [float("inf")] * (n + 1)
    
    q = deque([destination])
    level = 0
    while q:
        
        for _ in range(len(q)):
            cur = q.popleft()
            visited[cur] = min(visited[cur], level)
            for node in graph[cur]:
                if visited[node] == float("inf"):
                    q.append(node)
                    
        level += 1
        
    return [-1 if visited[start] == float("inf") else visited[start] for start in sources]
    
#     def dijkstra(start, dest):
#         q = [(0, start)]
#         visited = [float("inf")] * (n + 1)
#         visited[start] = 0
        
#         while q:
#             time, cur = heapq.heappop(q)
#             for node in graph[cur]:
#                 if time + 1 <= visited[node]:
#                     visited[node] = time + 1
#                     heapq.heappush(q, (time + 1, node))
                    
#         return -1 if visited[dest] == float("inf") else visited[dest]
    
#     return [dijkstra(start, destination) for start in sources]
