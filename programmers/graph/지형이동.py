import sys
sys.setrecursionlimit(10**6) # 재귀 에러 방지 필수!

def solution(land, height):
    N = len(land)
    groups = dict() # (x, y) : group_id
    
    # 1. 그룹핑 함수 (질문자님 스타일 수정)
    # 리턴값 없이 방문 체크만 수행합니다.
    def find_group(x, y, group_id):
        dirs = [1, 0, -1, 0, 1]
        groups[(x, y)] = group_id
        
        for i in range(4):
            dx, dy = dirs[i], dirs[i+1]
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                # 이미 방문한 곳은 패스
                if (nx, ny) in groups:
                    continue
                
                # 높이 차이가 height 이하라면 같은 그룹으로 계속 탐색
                if abs(land[x][y] - land[nx][ny]) <= height:
                    find_group(nx, ny, group_id)

    # 전체 맵을 돌며 그룹핑 실행
    group_cnt = 0
    for i in range(N):
        for j in range(N):
            if (i, j) not in groups:
                find_group(i, j, group_cnt)
                group_cnt += 1
                
    # 2. 그룹 간의 사다리(간선) 비용 구하기
    edges = []
    # 위아래오른쪽왼쪽
    dirs = [1, 0, -1, 0, 1]
    
    for x in range(N):
        for y in range(N):
            curr_g = groups[(x, y)]
            
            # 4방향 확인
            for i in range(4):
                nx, ny = x + dirs[i], y + dirs[i+1]
                if 0 <= nx < N and 0 <= ny < N:
                    next_g = groups[(nx, ny)]
                    
                    # 서로 다른 그룹이면 사다리 비용 저장
                    if curr_g != next_g:
                        diff = abs(land[x][y] - land[nx][ny])
                        edges.append((diff, curr_g, next_g))

    # 3. 크루스칼 알고리즘 (최소 비용 연결)
    edges.sort() # 비용이 싼 순서대로 정렬
    
    parent = [i for i in range(group_cnt)]
    
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        a = find(a)
        b = find(b)
        if a < b: parent[b] = a
        else: parent[a] = b
            
    res = 0
    cnt = 0
    
    for cost, a, b in edges:
        if find(a) != find(b):
            union(a, b)
            res += cost
            cnt += 1
            # 모든 그룹이 연결되면 끝 (간선 수 = 그룹 수 - 1)
            if cnt == group_cnt - 1:
                break
                
    return res
