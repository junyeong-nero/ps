from itertools import product

def solution(clockHands):
    n = len(clockHands)
    INF = float('inf')
    
    dirs = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def in_bound(x, y):
        return 0 <= x < n and 0 <= y < n
    
    def rotate(board, x, y, cnt):
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_bound(nx, ny):
                board[nx][ny] = (board[nx][ny] + cnt) % 4
    
    ans = INF
    
    for first_row in product(range(4), repeat=n):
        board = [row[:] for row in clockHands]
        total = 0
        
        # 첫 줄 적용
        for j in range(n):
            cnt = first_row[j]
            if cnt:
                rotate(board, 0, j, cnt)
                total += cnt
        
        # 2번째 줄부터는 강제 결정
        for i in range(1, n):
            for j in range(n):
                cnt = (4 - board[i - 1][j]) % 4
                if cnt:
                    rotate(board, i, j, cnt)
                    total += cnt
        
        # 마지막 줄 검사
        if all(board[n - 1][j] == 0 for j in range(n)):
            ans = min(ans, total)
    
    return ans
