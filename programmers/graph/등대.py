from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

def solution(n, lighthouse):
    
    graph = defaultdict(list)
    for u, v in lighthouse:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * (n + 1)
    dp = [[0, 0] for _ in range(n + 1)]
    
    def dfs(u):
        visited[u] = True
        
        dp[u][0] = 0      # u 선택 안함
        dp[u][1] = 1      # u 선택함
        
        for v in graph[u]:
            if not visited[v]:
                dfs(v)
                
                dp[u][0] += dp[v][1]
                dp[u][1] += min(dp[v][0], dp[v][1])
    
    dfs(1)  # 트리이므로 아무 노드에서 시작해도 됨
    
    return min(dp[1][0], dp[1][1])
