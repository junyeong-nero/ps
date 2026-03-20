from collections import defaultdict, deque

def solution(nodes, edges):
    graph = defaultdict(list)
    degree = defaultdict(int)

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1

    visited = set()
    res = [0, 0]

    for start in nodes:
        if start in visited:
            continue

        # 연결요소 수집
        comp = []
        q = deque([start])
        visited.add(start)

        while q:
            cur = q.popleft()
            comp.append(cur)
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)

        # 이 연결요소 내부에서만 A, cnt 계산
        cnt = [0, 0]
        A = {}

        for u in comp:
            A[u] = (u ^ degree[u]) & 1
            cnt[A[u]] += 1

        for u in comp:
            a = A[u]
            if cnt[a] == 1:
                res[a] += 1

    return res
    
    ### BFS
    
    n = len(nodes)
    
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)    

    def check(head):
        
        visited = set()
        q = deque([head])
        target = (head ^ len(graph[head])) & 1
        
        while q:
            
            cur = q.popleft()
            visited.add(cur)
            
            num_child = 0
            for node in graph[cur]:
                if node in visited:
                    continue
                num_child += 1
                q.append(node)
            
            temp = (cur ^ num_child) & 1
            if temp != target:
                return None
        
        return target
    
    res = [0, 0]
    for node in nodes:
        temp = check(node)
        if temp is not None:
            res[temp] += 1
        
    return res
