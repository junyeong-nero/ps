import sys
# Python의 기본 재귀 깊이 제한을 늘려줍니다 (런타임 에러 해결)
sys.setrecursionlimit(300000)
from collections import defaultdict

def solution(t):
    n = len(t)
    graph = defaultdict(list)
    
    for u, v in t:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [0] * (n + 1)
    
    # unique_count를 인자로 넘겨 O(1)로 고유 방문자 수를 계산 (시간 초과 해결)
    def check(node, unique_count):
        if visited[node] == 2:
            return 0
        
        # 처음 방문하는 노드일 때만 고유 개수 +1
        if visited[node] == 0:
            unique_count += 1
            
        visited[node] += 1
        
        res = unique_count
        for neigh in graph[node]:
            if visited[neigh] < 2:
                # 다음 노드로 넘어갈 때 갱신된 unique_count를 그대로 전달
                res = max(res, check(neigh, unique_count))
                
        visited[node] -= 1
        return res
    
    res = 0
    # 끝점(Leaf Node)에서만 탐색 시작
    leaf_nodes = [node for node in graph if len(graph[node]) == 1]
    
    # 노드가 1개이거나 간선이 없는 예외 처리
    if not leaf_nodes:
        leaf_nodes = list(graph.keys())
        
    for node in leaf_nodes:
        temp = check(node, 0)
        res = max(res, temp)
        
    return res
