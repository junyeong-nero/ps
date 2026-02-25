import heapq

def solution(n, start, end, roads, traps):
    # 1. 그래프 초기화 (정방향, 역방향 분리)
    graph = [[] for _ in range(n + 1)]
    rev_graph = [[] for _ in range(n + 1)]
    
    for u, v, c in roads:
        graph[u].append((v, c))
        rev_graph[v].append((u, c)) # 방향이 뒤집혔을 때 사용할 그래프
        
    trap_idx = {trap: i for i, trap in enumerate(traps)}
    
    # 방문 배열: distance[node][mask] = cost
    # 트랩의 최대 개수가 10개이므로 mask는 0 ~ 1023 (1<<10)
    INF = float('inf')
    distance = [[INF] * (1 << len(traps)) for _ in range(n + 1)]
    distance[start][0] = 0
    
    # 큐: (누적 비용, 현재 노드, 현재 트랩 상태 마스크)
    q = [(0, start, 0)]
    
    while q:
        time, curr, mask = heapq.heappop(q)
        
        # 목적지 도착 시 최단 시간 반환
        if curr == end:
            return time
        
        # 이미 더 적은 비용으로 해당 노드를 같은 트랩 상태로 방문했다면 스킵
        if distance[curr][mask] < time:
            continue
            
        # 현재 노드가 활성화된 트랩인지 확인
        curr_is_trap = False
        if curr in trap_idx:
            curr_is_trap = (mask & (1 << trap_idx[curr])) != 0
            
        # 다음 노드 탐색 (정방향 그래프와 역방향 그래프 모두 확인)
        # edges = [(다음 노드, 비용, 길의 원래 방향이 정방향인지 여부)]
        edges = []
        for v, c in graph[curr]:
            edges.append((v, c, True))
        for u, c in rev_graph[curr]:
            edges.append((u, c, False))
            
        for nxt, cost, is_forward in edges:
            # 다음 노드가 활성화된 트랩인지 확인
            nxt_is_trap = False
            if nxt in trap_idx:
                nxt_is_trap = (mask & (1 << trap_idx[nxt])) != 0
                
            # 길의 방향이 뒤집혔는지 여부 (둘 중 하나만 트랩이 활성화되어 있어야 뒤집힘 XOR)
            is_reversed = curr_is_trap ^ nxt_is_trap
            
            # 길이 뒤집혔는데 원래 정방향 길이거나, 길이 안 뒤집혔는데 원래 역방향 길이면 이동 불가
            if is_reversed == is_forward:
                continue
                
            # 다음 노드로 이동할 때의 마스크 계산
            nxt_mask = mask
            if nxt in trap_idx:
                nxt_mask ^= (1 << trap_idx[nxt])
                
            nxt_time = time + cost
            
            # 최단 거리가 갱신될 때만 큐에 추가
            if nxt_time < distance[nxt][nxt_mask]:
                distance[nxt][nxt_mask] = nxt_time
                heapq.heappush(q, (nxt_time, nxt, nxt_mask))
                
    return -1
