class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        m, n = len(mat), len(mat[0])
        
        def check(a, b):
            for i in range(m):
                for j in range(n):
                    if a[i][j] != b[i][j]:
                        return False
            
            return True

        def rotate(a):
            return [list(col)[::-1] for col in zip(*a)]

        for _ in range(4):
            if check(mat, target):
                return True
            mat = rotate(mat)

        return False
            
