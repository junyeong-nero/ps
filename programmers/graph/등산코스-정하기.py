from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    gates = set(gates)
    summits = set(summits)
    
    graph = [[] for _ in range(n + 1)]
    
    # gate는 진입 불가, summit은 출발 불가하도록 방향 제한
    for u, v, w in paths:
        if u in gates or v in summits:
            graph[u].append((v, w))
        elif v in gates or u in summits:
            graph[v].append((u, w))
        else:
            graph[u].append((v, w))
            graph[v].append((u, w))
    
    INF = float('inf')
    intensity = [INF] * (n + 1)
    pq = []
    
    # 멀티소스 다익스트라
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(pq, (0, gate))
    
    while pq:
        cur_intensity, node = heapq.heappop(pq)
        
        if cur_intensity > intensity[node]:
            continue
        
        if node in summits:
            continue
        
        for nxt, w in graph[node]:
            new_intensity = max(cur_intensity, w)
            if new_intensity < intensity[nxt]:
                intensity[nxt] = new_intensity
                heapq.heappush(pq, (new_intensity, nxt))
    
    answer = [0, INF]
    for summit in sorted(summits):
        if intensity[summit] < answer[1]:
            answer = [summit, intensity[summit]]
    
    return answer

# from collections import defaultdict, deque
# import heapq

# def solution(n, paths, gates, summits):
    
#     graph = defaultdict(list)
#     for u, v, w in paths:
#         graph[u].append((v, w))
#         graph[v].append((u, w))
        
#     # intensity 최소화하는 최단경로 찾기.
#     # 시작지점 = 끝지점 같아야 함
#     # 봉우리는 하나만 방문하도록.
#     # 쉼터 / 봉우리에서 휴식가능 
    
#     # 결국 시작지점 -> 봉우리 까지 가면서 거치는 edge의 최댓값 (intensity) 
#     # 를 최소화하는 문제.
    
#     # 근데 bi-directional 하기 때문에 가는데 걸리는 최솟값만 확인하면 됨.
#     # 어짜피 똑같은 길로 돌아오면 되니까.
    
#     # 시작점 -> 끝점
    
#     target = float("inf")
#     target_idx = -1 
    
#     def func(start):
        
#         nonlocal target, target_idx
#         q = [(0, start)]
        
#         visited = [float("inf")] * (n + 1)
#         visited[start] = 0
        
#         while q:
#             intensity, location = heapq.heappop(q)
#             if location in summits:
#                 if intensity < target:
#                     target = intensity
#                     target_idx = location
#                 elif intensity == target:
#                     target_idx = min(target_idx, location)
#                 continue
                
#             if intensity > target:
#                 continue
                
#             for node, weight in graph[location]:
#                 new_intensity = max(intensity, weight)
#                 if new_intensity < visited[node]:
#                     visited[node] = new_intensity
#                     heapq.heappush(q, (new_intensity, node))
        
#         return target, target_idx

#     for gate in gates:
#         func(gate)
        
#     return [target_idx, target]
