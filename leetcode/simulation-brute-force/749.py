from collections import deque
import heapq

class Solution:
    def containVirus(self, board: list[list[int]]) -> int:
        m, n = len(board), len(board[0])
        res = 0

        while True:
            visited = set()
            regions = [] # (영향을 주는 빈칸 수, 필요한 벽 수, 바이러스 좌표들, 감염시킬 빈칸들)

            for i in range(m):
                for j in range(n):
                    if board[i][j] == 1 and (i, j) not in visited:
                        # 한 바이러스 구역을 BFS로 탐색
                        region_cells = set()
                        frontiers = set() # 이 구역이 감염시킬 빈칸(중복 제거)
                        walls = 0
                        
                        q = deque([(i, j)])
                        visited.add((i, j))
                        region_cells.add((i, j))
                        
                        while q:
                            r, c = q.popleft()
                            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                                nr, nc = r + dr, c + dc
                                if 0 <= nr < m and 0 <= nc < n:
                                    if board[nr][nc] == 1 and (nr, nc) not in visited:
                                        visited.add((nr, nc))
                                        region_cells.add((nr, nc))
                                        q.append((nr, nc))
                                    elif board[nr][nc] == 0:
                                        walls += 1
                                        frontiers.add((nr, nc))
                        
                        if frontiers:
                            # 영향을 주는 빈칸이 많은 순으로 정렬하기 위해 음수로 저장 (Max-Heap 효과)
                            regions.append((-len(frontiers), walls, region_cells, frontiers))

            if not regions:
                break
            
            # 1. 가장 위험한 지역 선택 (영향을 주는 빈칸이 가장 많은 곳)
            regions.sort()
            _, walls_needed, isolate_cells, _ = regions.pop(0)
            res += walls_needed
            
            # 2. 선택된 지역 격리 (상태를 2로 변경하여 다시는 탐색되지 않게 함)
            for r, c in isolate_cells:
                board[r][c] = 2
            
            # 3. 나머지 지역들 확산
            for _, _, _, frontiers in regions:
                for r, c in frontiers:
                    board[r][c] = 1
                    
        return res
