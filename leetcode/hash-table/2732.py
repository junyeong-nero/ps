class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:

        m, n = len(grid), len(grid[0])

        # select k rows
        # each sum of rows should be less than or equal to float(k / 2)
        
        #  V V V V
        # [0,1,1,0] <
        # [0,0,0,1] < 
        # [1,1,1,1]

        # m = 10^4
        # n = 5

        # how to select row indices?
        # bitwise-DP : no
        # brute force : no
        # sliding window?

        d = dict()

        for i in range(m):

            val = 0
            for j in range(n):
                if grid[i][j]:
                    val |= (1 << j)
            
            if val == 0:
                return [i]
            
            for j in range(1, 32):
                if val & j == 0 and j in d:
                    return [d[j], i]

            d[val] = i
                
        return []
