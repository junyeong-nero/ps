from collections import defaultdict, deque

def solution(tickets):
    
    G = defaultdict(dict)
    n = len(tickets)
    for u, v in sorted(tickets, reverse=True): 
        G[u][v] = G[u].get(v, 0) + 1

    hist = []
    res = []
    
    def dfs(cur):
        nonlocal hist, res
        
        hist.append(cur)
        if len(hist) == n + 1:
            res = hist[:]
        
        for node, num in G[cur].items():
            if num <= 0:
                continue
            G[cur][node] -= 1
            dfs(node)
            G[cur][node] += 1
        hist.pop()
        
    dfs("ICN")
    return res
