from typing import List
from collections import defaultdict
import heapq

class Solution:
    def minMaxWeight(self, n: int, edges: List[List[int]], threshold: int) -> int:
        # 1. 그래프 구성 (Reverse Graph)
        # 원래 문제: 모든 노드 -> 0번 노드 (각 노드당 나가는 간선 최대 threshold개)
        # 변형 문제: 0번 노드 -> 모든 노드 (각 노드로 들어오는 간선 1개를 선택해 트리 구성)
        # v -> u 방향으로 저장하며, 동일 간선이 있다면 최소 가중치만 유지합니다.
        graph = defaultdict(dict)
        for u, v, w in edges:
            if u not in graph[v] or w < graph[v][u]:
                graph[v][u] = w
        
        # 2. 프림(Prim) 알고리즘 변형 (Min-Max Spanning Tree)
        # (가중치, 노드)
        min_heap = [(0, 0)]
        visited = [False] * n
        max_weight_in_path = 0
        visited_count = 0
        
        while min_heap:
            weight, u = heapq.heappop(min_heap)
            
            if visited[u]:
                continue
            
            # 방문 처리
            visited[u] = True
            visited_count += 1
            max_weight_in_path = max(max_weight_in_path, weight)
            
            # 모든 노드를 방문했다면 현재까지의 최대 가중치 반환
            if visited_count == n:
                return max_weight_in_path
            
            # 인접 노드 탐색
            for v, w in graph[u].items():
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))
                    
        # 모든 노드를 방문하지 못했다면 불가능
        return -1
