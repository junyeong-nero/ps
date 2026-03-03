from collections import defaultdict

def solution(board):
    n = len(board)
    blocks = defaultdict(set)
    
    # 1. 문제 해결: 빈 공간(0)은 블록으로 저장하지 않음
    for y in range(n):
        for x in range(n):
            if board[y][x] != 0:
                blocks[board[y][x]].add((x, y))
    
    def is_removable(block_index):
        if not blocks[block_index]:
            return False
        
        # x_coords에 중복이 많으므로 고유한 x열만 추출
        x_coords = [x for x, y in blocks[block_index]]
        y_coords = [y for x, y in blocks[block_index]]
        unique_x = list(set(x_coords))
        
        target_y = max(y_coords)
        
        # 작성하신 훌륭한 아이디어: 밑바닥이 모두 내 블록으로 평평한지 확인
        check = all(board[target_y][x] == block_index for x in unique_x)
        if not check:
            return False
        
        # 2. 문제 해결: 방해물 검사는 "검은 블록이 떨어질 빈 공간" 위쪽만 해야 함
        empty_col_count = 0 
        for x in unique_x:
            # 블록의 가장 밑바닥(target_y)의 바로 윗칸이 내 블록이 아니라면, 
            # 그곳이 바로 검은 블록이 떨어져 채워져야 할 "빈 공간"임
            if (x, target_y - 1) not in blocks[block_index]:
                empty_col_count += 1
                # 빈 공간이 있는 열의 위쪽만 방해물이 있는지 검사
                for y in range(target_y - 1, -1, -1):
                    if board[y][x] != 0:
                        return False
                        
        # 채울 빈 공간이 없는 꽉 찬 블록(예: 2x2 정사각형 등)은 제거 대상이 아님
        if empty_col_count == 0:
            return False
            
        return True
    
    def remove(block_index):
        for x, y in blocks[block_index]:
            board[y][x] = 0
        blocks[block_index].clear() # 데이터를 비워 다음 번에 False가 되도록 처리
    
    count = 0
    while True:
        changed = False
        # 3. 문제 해결: 딕셔너리 keys() 순회 시 list로 감싸서 안전하게 순회
        for block_id in list(blocks.keys()):
            if is_removable(block_id):
                changed = True
                remove(block_id)
                count += 1
                
        if not changed:
            break
        
    return count
