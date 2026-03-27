class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        
        m, n = len(mat), len(mat[0])

        def check(k):
            start_even = k % n
            start_odd = (-k + n * n) % n

            for i in range(m):
                for j in range(n):
                    d = start_even if i % 2 == 0 else start_odd
                    if mat[i][j] != mat[i][(j + d) % n]:
                        return False
            
            return True

        return check(k)
