import sys

# 재귀 깊이 늘리기 (Python 필수)
sys.setrecursionlimit(200000)

class DSU:
    def __init__(self, n, max_queries):
        # 원소 이동을 위해 넉넉한 크기의 parent 배열 생성 (최대 N + 쿼리 수)
        self.parent = list(range(n + max_queries + 1))
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x]) # 경로 압축
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parent[px] = py

def solution(n, queries):
    # DSU 초기화 (N + 쿼리 수 만큼 노드 공간 확보)
    dsu = DSU(n, len(queries))
    
    # 실제 원소 번호가 현재 사용 중인 DSU 노드 번호를 가리키는 매핑 배열
    # 초기에는 i번 원소 -> i번 노드
    idx_map = list(range(n + 1))
    
    # 새로운 노드 번호 할당을 위한 카운터
    next_node = n + 1 
    
    res = []
    
    for query in queries:
        t = query[0]
        
        if t == 1: # Union (집합 합치기: x가 속한 그룹 전체를 y로)
            x, y = query[1], query[2]
            dsu.union(idx_map[x], idx_map[y])
            
        elif t == 2: # Move (원소 이동: x 원소만 쏙 빼서 y로)
            # 이 부분이 핵심입니다.
            x, y = query[1], query[2]
            u, v = idx_map[x], idx_map[y]
            
            # x가 속했던 그룹에서 x만 분리하기 위해
            # x에게 새로운 노드 번호를 부여합니다.
            idx_map[x] = next_node
            next_node += 1
            
            # 새로운 x를 y 그룹에 병합
            dsu.union(idx_map[x], idx_map[y])
            
        elif t == 3: # Check
            x, y = query[1], query[2]
            if dsu.find(idx_map[x]) == dsu.find(idx_map[y]):
                res.append("Yes")
            else:
                res.append("No")
                
    return res
