class Solution:

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        left, right = 0, n - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            # Find row index of max element in mid column
            max_row = 0
            for i in range(m):
                if mat[i][mid] > mat[max_row][mid]:
                    max_row = i
            
            # Check left and right neighbors
            left_is_bigger = mid - 1 >= 0 and mat[max_row][mid - 1] > mat[max_row][mid]
            right_is_bigger = mid + 1 < n and mat[max_row][mid + 1] > mat[max_row][mid]
            
            if not left_is_bigger and not right_is_bigger:
                return [max_row, mid]
            elif right_is_bigger:
                left = mid + 1
            else:
                right = mid - 1


    # O (mn)
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        m, n = len(mat), len(mat[0])
        visited = set()
        
        def dfs(x, y):
            visited.add((x, y))
            dirs = [1, 0, -1, 0, 1]
            count = 0
            for i in range(4):
                nx, ny = x + dirs[i], y + dirs[i + 1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if (nx, ny) in visited:
                    continue
                if mat[nx][ny] > mat[x][y]:
                    count += 1
                    if temp := dfs(nx, ny):
                        return temp

            return (x, y) if count == 0 else None

        res = dfs(0, 0)
        return list(res)

