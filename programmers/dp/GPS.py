def solution(n, m, edge_list, k, gps_log):
    INF = float('inf')
    
    # 1. 그래프 구성 (인접 리스트)
    # n이 작으므로 dict보다 list가 접근 속도가 빠름
    graph = [[] for _ in range(n + 1)]
    for u, v in edge_list:
        graph[u].append(v)
        graph[v].append(u)
        
    # [Point] 제자리에 머무르는 경우(Self-loop) 추가
    for i in range(1, n + 1):
        graph[i].append(i)

    # 2. DP 초기화 (첫 번째 단계)
    # prev_dp[i]: 이전 시간 t-1에 i번 노드에 있을 최소 비용
    prev_dp = [INF] * (n + 1)
    start_node = gps_log[0]
    prev_dp[start_node] = 0

    # 3. DP 수행 (시간 t: 1 ~ k-1)
    for t in range(1, k):
        target = gps_log[t]
        curr_dp = [INF] * (n + 1)
        
        # 모든 노드(node)에 대해, 이전 단계에서 이 노드로 올 수 있는 경우를 확인
        for node in range(1, n + 1):
            # node로 연결된 인접 노드들(neighbor)의 이전 비용 중 최소값 찾기
            # (양방향 그래프이므로 graph[node]는 node로 들어올 수 있는 노드 목록과 같음)
            
            # Pythonic한 min 값 찾기:
            # 이전 단계(prev_dp)에서 node로 올 수 있는 인접 노드들의 비용들을 모음
            candidates = [prev_dp[neighbor] for neighbor in graph[node]]
            
            min_prev_cost = min(candidates)
            
            if min_prev_cost != INF:
                # 현재 위치(node)가 로그(target)와 다르면 비용 +1
                add_cost = 0 if node == target else 1
                curr_dp[node] = min_prev_cost + add_cost
        
        # 현재 단계를 이전 단계로 갱신 (Rolling Update)
        prev_dp = curr_dp

    # 4. 결과 반환
    # 마지막 시간(k-1)에 gps_log의 마지막 위치에 도달하는 비용
    end_node = gps_log[-1]
    result = prev_dp[end_node]
    
    return result if result != INF else -1
