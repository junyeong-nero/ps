def solution(board, commands):
    
    # 1. 움직이는 위젯을 옮김 
    # 2. 만약 움직이는 방향에 이미 위젯이 있는 경우, 연쇄적으로 위젯을 밀어야 함.
    # 3. 만약 위젯이 보드 바깥으로 나간다면, 반대쪽으로 이동시켜야 함.
    
    N, M = len(board), len(board[0])
    
    directions = [None, (0, 1), (1, 0), (0, -1), (-1, 0)]
    widget = dict()
    widget_size = dict()
    
    for i in range(N):
        for j in range(M):
            
            cur = board[i][j]
            if cur == 0: continue
            if cur not in widget:
                widget[cur] = (i, j)
                widget_size[cur] = 1
            else:
                x, y = widget[cur]
                widget_size[cur] = max(i - x + 1, j - y + 1)
    
    def visualize():
        
        board = [[0 for _ in range(M)] for _ in range(N)]
        for w_id in widget:
            x, y = widget[w_id]
            size = widget_size[w_id]
            
            for i in range(x, x + size):
                for j in range(y, y + size):
                    board[i % N][j % M] = w_id
                    
        return board
    
    
    def get_boundary(ID):
        x1, y1 = widget[ID]
        x2, y2 = x1 + widget_size[ID] - 1, y1 + widget_size[ID] - 1
        return (x1, y1, x2, y2)
    
    def _on_board(x, y):
        return 0 <= x < N and 0 <= y < M
    
    def on_board(ID):
        x, y = widget[ID]
        size = widget_size[ID]
        return _on_board(x, y) and _on_board(x + size - 1, y + size - 1)
    
    def _is_overlap(rect1, rect2):
        x1, y1, x2, y2 = rect1
        x3, y3, x4, y4 = rect2
        
        L = max(x1, x3)
        R = min(x2, x4)
        T = max(y1, y3)
        B = min(y2, y4)
            
        return L <= R and T <= B
    
    def is_overlap(ID1, ID2):
        rect1, rect2 = get_boundary(ID1), get_boundary(ID2)
        return _is_overlap(rect1, rect2)

    
    def find_overlap_widgets(ID):
        
        d = set()
        for w_id in widget:
            if w_id == ID: continue
            if is_overlap(w_id, ID):
                d.add(w_id)
                
        return d
    
    def push(ID, d_ID, check_collision=False):
            
        dx, dy = directions[d_ID]
        x, y = widget[ID]
        
        nx, ny = x + dx, y + dy
        widget[ID] = (nx, ny)
        
        if not on_board(ID):        
            if dx == 1:
                nx = 0
            if dx == -1:
                nx = N - widget_size[ID]
            if dy == 1:
                ny = 0
            if dy == -1:
                ny = M - widget_size[ID] 
            widget[ID] = (nx, ny)
            
        if check_collision:
            collision(ID, d_ID)
                
                
    def collision(ID, d_ID):
        while True:
            overlap_ids = find_overlap_widgets(ID)
            if not overlap_ids:
                return

            for t_id in list(overlap_ids):
                while is_overlap(t_id, ID):
                    push(tㅊ_id, d_ID)
                collision(t_id, d_ID)

    
    for ID, w_ID in commands:
        
        push(ID, w_ID, check_collision=True)
        # print("push", ID, w_ID)
        # print(*visualize(), sep="\n")
        
    return visualize()
