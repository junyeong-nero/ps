from collections import defaultdict, deque

def solution(a, edges):
    # 1. 총합이 0이 아니면 불가능
    if sum(a) != 0:
        return -1
    
    n = len(a)
    graph = defaultdict(list)
    # 진입 차수(연결된 간선의 수) 계산
    degree = [0] * n
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
        degree[u] += 1
        degree[v] += 1
        
    # 2. 리프 노드(연결된 간선이 1개인 노드)를 큐에 넣음
    # 모든 노드가 0인 경우(n=1 등) 고려하지 않아도 됨 (문제 조건상 n>=2)
    queue = deque()
    for i in range(n):
        if degree[i] == 1:
            queue.append(i)
            
    res = 0
    
    # 3. 위상 정렬과 유사하게 수행
    while queue:
        cur = queue.popleft()
        
        # 현재 노드의 가중치 절댓값을 결과에 더함
        res += abs(a[cur])
        
        # 현재 노드와 연결된 이웃(부모) 찾기
        for neighbor in graph[cur]:
            if degree[neighbor] == 0: # 이미 처리된 노드는 건너뜀
                continue
            
            # 가중치를 이웃에게 토스
            a[neighbor] += a[cur]
            
            # 현재 노드는 처리되었으므로 간선 끊기 (이웃의 차수 감소)
            degree[neighbor] -= 1
            
            # 이웃 노드가 이제 리프 노드가 되었다면(자식들이 다 처리됐다면) 큐에 추가
            if degree[neighbor] == 1:
                queue.append(neighbor)
                
            # 트리는 사이클이 없으므로, 처리되지 않은 유일한 이웃이 부모임.
            # 따라서 부모를 찾으면 루프 종료 (최적화)
            break
            
        # 현재 노드 삭제 처리 (실제 삭제 대신 차수를 0으로 만들어 무효화)
        degree[cur] = 0
                    
    return res
