class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        temp = []
        for column in zip(*matrix):
            temp.append(list(column)[::-1])
        
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[i][j]
