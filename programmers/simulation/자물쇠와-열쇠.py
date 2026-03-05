def rotate_90(matrix):
    return [list(row) for row in zip(*matrix[::-1])]

def check(x, y, M, N, key, board):
    # board에 key 더하기
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] += key[i][j]
            
    # 중앙 N x N 영역이 모두 1인지 확인
    is_valid = True
    for i in range(N, 2 * N):
        for j in range(N, 2 * N):
            if board[i][j] != 1:
                is_valid = False
                break
        if not is_valid: break
        
    # board 원상 복구 (다음 시도를 위해)
    for i in range(M):
        for j in range(M):
            board[x + i][y + j] -= key[i][j]
            
    return is_valid

def solution(key, lock):
    M, N = len(key), len(lock)
    # 3배 큰 보드 생성 및 중앙에 lock 배치
    board = [[0] * (3 * N) for _ in range(3 * N)]
    for i in range(N):
        for j in range(N):
            board[N + i][N + j] = lock[i][j]
            
    # 4방향 회전
    for _ in range(4):
        # 모든 시작점 시도 (0부터 2*N까지)
        for x in range(2 * N):
            for y in range(2 * N):
                if check(x, y, M, N, key, board):
                    return True
        key = rotate_90(key)
        
    return False

# def encode(pattern, target=0, dirs=0):
#     n = len(pattern)
#     d = []
#     if dirs == 0:
#         for x in range(n):
#             for y in range(n):
#                 if pattern[x][y] != target:
#                     continue
#                 d.append((x, y))
#     if dirs == 1:
#         for y in range(n):  
#             for x in range(n):
#                 if pattern[n - 1 - x][y] != target:
#                     continue
#                 d.append((x, y))
#     if dirs == 2:
#         for x in range(n):
#             for y in range(n):  
#                 if pattern[n - 1 - x][n - 1 - y] != target:
#                     continue
#                 d.append((x, y))
#     if dirs == 3:
#         for y in range(n):      
#             for x in range(n):
#                 if pattern[x][n - 1 - y] != target:
#                     continue
#                 d.append((x, y))
            
#     base = min(d)
#     d = {(x - base[0], y - base[1]) for x, y in d}
#     return d, base


# def solution(key, lock):
#     N, M = len(lock), len(key)
    
#     emb_lock, base = encode(lock)
#     for dirs in range(4):
#         emb_key, _ = encode(key, target=1, dirs=dirs)
#         # print(emb_lock, emb_key, dirs)
#         if emb_lock.issubset(emb_key):
#             key = emb_key - emb_lock
#             key = [(base[0] + x, base[1] + y) for x, y in key]
#             check = all([x < 0 or x >= N or y < 0 or y >= N for x, y in key])
#             if check:
#                 return True
    
#     return False
