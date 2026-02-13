from collections import defaultdict

def solution(board, skill):
    
    n, m = len(board), len(board[0])
    hist_a = defaultdict(dict)
    
    for type, r1, c1, r2, c2, degree in skill:
        neg = 1 if type == 2 else -1
        hist_a[r1][c1] = hist_a[r1].get(c1, 0) + neg * degree
        hist_a[r1][c2 + 1] = hist_a[r1].get(c2 + 1, 0) - neg * degree
        
        hist_a[r2 + 1][c1] = hist_a[r2 + 1].get(c1, 0) - neg * degree
        hist_a[r2 + 1][c2 + 1] = hist_a[r2 + 1].get(c2 + 1, 0) + neg * degree
        
    count = 0
    diff = [0] * m
    for x in range(n):
        
        cur = 0
        for y in range(m):
            cur += hist_a[x].get(y, 0)
            diff[y] += cur
        
        for y in range(m):
            board[x][y] += diff[y]
            if board[x][y] > 0:
                count += 1
        
    # print(board)
    return count





