def solution(visible, hidden, k):
    
    m, n = len(visible), len(visible[0])
    flip_columns = set()
    
    def get_point(x, y, row_flipped=False):
        col_flipped = x in flip_columns
        flipped = col_flipped ^ row_flipped
        return hidden[x][y] if flipped else visible[x][y]
    
    def best_row_sum():
        total = 0
        flip_rows = set()
        
        for j in range(n):
            normal = sum(get_point(i, j, False) for i in range(m))
            flipped = sum(get_point(i, j, True) for i in range(m))
            if flipped - k > normal:
                total += flipped - k
                flip_rows.add(j)
            else:
                total += normal
        
        if m % 2 == 0 and n % 2 == 0:
            min_value = float("inf")
            for i in range(m):
                for j in range(n):
                    if (i == 0 and j == 0) or (i == m-1 and j == n-1):
                        continue
                    row_flipped = j in flip_rows
                    min_value = min(min_value, get_point(i, j, row_flipped))
            total -= min_value
        
        return total - k * len(flip_columns)
    
    def dfs_col(col_idx):
        if col_idx == m:
            return best_row_sum()
        
        res = dfs_col(col_idx + 1)
        flip_columns.add(col_idx)
        res = max(res, dfs_col(col_idx + 1))
        flip_columns.remove(col_idx)
        return res
    
    return dfs_col(0)
