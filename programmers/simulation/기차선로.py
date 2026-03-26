def solution(grid):
    
    # n, m 범위가 좁다. -> DFS 로 풀어도 됨
    # DP 사용...은 못할 것 같음 (구현 이슈, 최적화 할 때는 가능)
    # 3번 선로가 까다롭다. 상하좌우 다 연결되어야 함.
    # 3번 선로를 쓴느 순간, 이 좌표는 2번 지나갈 수 있게 됨. 
    # 그리고 가로 방향, 세로방향으로 지나가야 하는데... 이게 문제구만.
    
    m, n = len(grid), len(grid[0])
    
    def onboard(x, y):
        return 0 <= x < m and 0 <= y < n

    #   1
    # 2   0
    #   3
    
    # dirc -> tile, new_dirc
    avail_tiles = {
        0: [(1, 0), (3, 0), (4, 1), (7, 3)],
        1: [(2, 1), (3, 1), (6, 0), (7, 2)],
        2: [(1, 2), (3, 2), (5, 1), (6, 3)],
        3: [(2, 3), (3, 3), (4, 2), (5, 0)],
    }
    
    moves = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    
    
    type3_tiles = dict()
    original_tiles = dict()
    for i in range(m):
        for j in range(n):
            if grid[i][j] > 0:
                original_tiles[(i, j)] = 0
    
                
    def dfs(x, y, dirc=0):
        
        if (x, y) in original_tiles:
            original_tiles[(x, y)] += 1
        
        if x == m - 1 and y == n - 1:
            # print(grid)
            for value in original_tiles.values():
                if value == 0:
                    return 0
                
            for x, y in type3_tiles:
                if type3_tiles[(x, y)][0] != 1 or type3_tiles[(x, y)][1] != 1:
                    return 0
            
            return 1
    
        res = 0
        for tile_type, new_dirc in avail_tiles[dirc]:
            
            dx, dy = moves[dirc]
            nx, ny = x + dx, y + dy
            
            if not onboard(nx, ny): continue
            if grid[nx][ny] == -1: continue
            
            if grid[nx][ny] == 0:
                
                grid[nx][ny] = tile_type
                
                if tile_type == 3:
                    if (nx, ny) not in type3_tiles:
                        type3_tiles[(nx, ny)] = [0, 0]
                    type3_tiles[(nx, ny)][new_dirc & 1] += 1
                
                res += dfs(nx, ny, new_dirc)
                
                if tile_type == 3:
                    type3_tiles[(nx, ny)][new_dirc & 1] -= 1
                    if type3_tiles[(nx, ny)][0] == 0 and type3_tiles[(nx, ny)][1] == 0:
                        del type3_tiles[(nx, ny)]
                
                
                grid[nx][ny] = 0
                
            elif grid[nx][ny] == tile_type:
                
                if tile_type == 3:
                    if (nx, ny) not in type3_tiles:
                        type3_tiles[(nx, ny)] = [0, 0]
                    type3_tiles[(nx, ny)][new_dirc & 1] += 1
                
                res += dfs(nx, ny, new_dirc)
                
                if tile_type == 3:
                    type3_tiles[(nx, ny)][new_dirc & 1] -= 1
                    if type3_tiles[(nx, ny)][0] == 0 and type3_tiles[(nx, ny)][1] == 0:
                        del type3_tiles[(nx, ny)]
                
        if (x, y) in original_tiles:
            original_tiles[(x, y)] -= 1
        
        return res
    
    answer = dfs(0, 0)
    return answer
