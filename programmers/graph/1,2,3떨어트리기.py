from collections import defaultdict

def solution(edges, target):
    n = len(edges) + 1  # 노드 개수는 간선 수 + 1
    tree = defaultdict(list)
    
    # 트리 구성
    for u, v in edges:
        tree[u].append(v)
    
    # 자식 노드 번호 순 정렬 (문제 조건)
    for u in tree:
        tree[u].sort()
        
    # 각 노드의 현재 자식 인덱스 (라우터 상태)
    cur_child_idx = [0] * (n + 1)
    
    # 각 리프 노드에 떨어진 공의 개수
    counts = [0] * (n + 1)
    
    # 공이 떨어진 리프 노드의 순서 기록
    visit_order = []
    
    # Phase 1: 공을 떨어뜨리며 최소 조건 만족할 때까지 시뮬레이션
    while True:
        # 1. 모든 리프 노드가 조건을 만족하는지 검사
        check = True
        for i in range(1, n + 1):
            # target이 있는 노드인데, 
            # (현재 공 개수 > target) -> 불가능 (1만 넣어도 초과)
            if counts[i] > target[i-1]:
                return [-1]
            
            # (현재 공 개수 * 3 < target) -> 아직 부족함 (3만 넣어도 부족)
            # 이 조건이 하나라도 있으면 더 던져야 함
            if target[i-1] > 3 * counts[i]:
                check = False
        
        if check:
            break
            
        # 2. 공 떨어뜨리기 (라우팅)
        curr = 1
        # 리프 노드가 아닐 때까지 이동
        while tree[curr]:
            next_node = tree[curr][cur_child_idx[curr]]
            # 다음을 위해 라우터 방향 변경
            cur_child_idx[curr] = (cur_child_idx[curr] + 1) % len(tree[curr])
            curr = next_node
        
        # 리프 노드 도착
        counts[curr] += 1
        visit_order.append(curr)
    
    # Phase 2: 방문 순서대로 값을 1, 2, 3 중 가장 작은 것으로 채우기
    result = []
    
    for node in visit_order:
        counts[node] -= 1  # 이 노드에 던져야 할 남은 공의 개수 감소
        val = 0
        
        # 1을 선택할 수 있는가?
        # (남은 target - 1)이 (남은 공 개수 * 3)보다 작거나 같아야 함.
        # 즉, 여기서 1을 써도 나중에 3씩 꽉 채워서 복구가 가능해야 함.
        if target[node-1] - 1 <= 3 * counts[node]:
            val = 1
        # 2를 선택할 수 있는가?
        elif target[node-1] - 2 <= 3 * counts[node]:
            val = 2
        # 안되면 3
        else:
            val = 3
            
        target[node-1] -= val
        result.append(val)
        
    return result
