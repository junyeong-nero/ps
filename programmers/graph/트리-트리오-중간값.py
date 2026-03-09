from collections import deque

def solution(n, edges):
    # 1. 그래프 생성
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        
    # BFS 함수 정의 (시작 노드로부터의 최대 거리와, 그 거리에 있는 노드 리스트 반환)
    def bfs(start):
        distances = [-1] * (n + 1)
        distances[start] = 0
        q = deque([start])
        max_dist = 0
        
        while q:
            curr = q.popleft()
            for neighbor in graph[curr]:
                if distances[neighbor] == -1:
                    distances[neighbor] = distances[curr] + 1
                    max_dist = max(max_dist, distances[neighbor])
                    q.append(neighbor)
                    
        # 가장 멀리 있는 노드들 추출
        farthest_nodes = [i for i, d in enumerate(distances) if d == max_dist]
        return max_dist, farthest_nodes

    # Step 1: 임의의 노드(1)에서 가장 먼 노드(A) 찾기
    _, farthest_from_1 = bfs(1)
    A = farthest_from_1[0]
    
    # Step 2: A에서 가장 먼 노드들 찾기 (이때의 max_dist 가 트리의 지름 D가 됨)
    D, farthest_from_A = bfs(A)
    
    # Step 3: A에서 거리가 D인 노드가 2개 이상이라면, 중간값은 D
    if len(farthest_from_A) >= 2:
        return D
        
    # Step 4: A에서 거리가 D인 노드가 1개라면(B), B에서 다시 확인
    B = farthest_from_A[0]
    D_B, farthest_from_B = bfs(B)
    
    # Step 5: B에서 거리가 D인 노드가 2개 이상이라면, 중간값은 D
    if len(farthest_from_B) >= 2:
        return D
        
    # Step 6: 지름 경로가 완벽히 유일하다면 중간값은 D-1
    return D - 1


# from collections import Counter, defaultdict, deque
# from itertools import combinations

# def solution(n, edges):

#     # n = 25 * 10^4 => matrix 형태로는 못만듬.
#     # a b c 순서는 상관없음.
#     # intuitive 하게 그냥 leaf node 끼리 연결하면 가장 길지 않을까?
#     # common ancestor 를 찾는 문제.
    
#     graph = defaultdict(list)
#     for u, v in edges:
#         graph[u].append(v)
#         graph[v].append(u)
    
#     leaves = [node for node, value in graph.items() if len(value) == 1]
#     # print(leaves)
    
#     dist_map = dict()
    
#     def distance(a):
#         visited = set()
#         q = deque([(a, 0)])
        
#         while q:
#             cur, dist = q.popleft()
#             if cur in leaves:
#                 dist_map[(a, cur)] = dist
#                 dist_map[(cur, a)] = dist
            
#             visited.add(cur)
#             for node in graph[cur]:
#                 if node in visited:
#                     continue
#                 q.append((node, dist + 1))  
        
#         return -1

#     # 근데 왜 중간값이지?
#     # a b 가 고정되어있고, c 를 추가한다고 생각했을 
    
#     if len(leaves) < 3:
#         leaves = list(range(1, n + 1))
        
#     for leaf in leaves:
#         distance(leaf)

#     def func(a, b, c):
#         return sorted([dist_map[(a, b)], dist_map[(c, b)], dist_map[(a, c)]])[1]
    
#     res = 0
#     for a, b, c in combinations(leaves, 3):
#         temp = func(a, b, c)
#         res = max(res, temp)
        
#     return res
