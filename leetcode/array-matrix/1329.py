class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        # x - y = k
        # x = k + y
        # k in [-n, m]
        for k in range(-n, m + 1):
            
            # print(k)
            arr = []

            # 0 <= x = k + y < m
            for y in range(max(0, -k), min(n, m - k)):
                x = k + y
                arr.append(mat[x][y])
                # print(x, y, mat[x][y])

            arr = sorted(arr)
            # print(arr)

            index = 0
            for y in range(max(0, -k), min(n, m - k)):
                x = k + y
                mat[x][y] = arr[index]
                index += 1

        return mat
