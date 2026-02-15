from collections import deque

def solution(rc, operations):
    n, m = len(rc), len(rc[0])

    L = deque(row[0] for row in rc)
    R = deque(row[-1] for row in rc)
    M = deque(deque(row[1:-1]) for row in rc)  # m==2면 각 행이 빈 deque

    def shift_row():
        L.appendleft(L.pop())
        R.appendleft(R.pop())
        M.appendleft(M.pop())

    def rotate():
        if m == 2:
            # O(1) perimeter rotate for 2 columns
            x = L.popleft()
            R.appendleft(x)
            y = R.pop()
            L.append(y)
            return

        # m >= 3 : O(1)
        M[0].appendleft(L.popleft())
        R.appendleft(M[0].pop())
        M[-1].append(R.pop())
        L.append(M[-1].popleft())

    for op in operations:
        if op == "ShiftRow":
            shift_row()
        else:
            rotate()

    return [[L[i]] + list(M[i]) + [R[i]] for i in range(n)]


# from collections import deque

# def solution(rc, operations):
#     board = deque([deque(row) for row in rc])
    
#     def shift_row():
#         tar = board.pop()
#         board.appendleft(tar)
        
#     def rotate():
#         first_column = [row[0] for row in board]
#         last_column = [row[-1] for row in board]
#         board[0].appendleft(board[0].pop())
#         board[-1].append(board[-1].popleft())
        
#         n = len(board)
#         for i in range(n):
#             if i + 1 < n:
#                 board[i][0] = first_column[i + 1]
#             if i + 1 < n:
#                 board[i + 1][-1] = last_column[i]
        
    
#     funcs = {
#         "ShiftRow": shift_row,
#         "Rotate": rotate
#     }
    
#     for op in operations:
#         funcs[op]()
    
#     answer = [list(row) for row in board]
#     return answer
