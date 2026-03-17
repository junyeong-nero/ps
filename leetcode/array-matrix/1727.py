# My Solution with Subset Indices

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        # rearrange columns of matrix
        # matrix size <= 10^5

        # 어떻게 rearrange 를 하지?
        # i 번째 row 이 1 인 columns의 indices.
        # i + 1 번째 row 이 1 인 columns 의 indices.
        # i + 2 번째 row 이 1 인 ....

        # indices 를 intersect 하면 결국 width 가 나온다.

        d = [set() for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    d[i].add(j)

        # O(m * n)
        def check(row_index):
            subset = d[row_index]
            index = row_index + 1
            res = len(subset)

            while subset and index < m:
                subset = subset & d[index]
                curr = (index - row_index + 1) * len(subset)
                res = max(res, curr)
                index += 1

            return res, index

        res = 0
        i = 0
        while i < m:
            temp, _ = check(i)
            res = max(res, temp)
            i += 1

        return res


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            # 1) 현재 row까지의 연속 높이 누적
            for j in range(n):
                if matrix[i][j] == 0:
                    heights[j] = 0
                else:
                    heights[j] += 1

            # 2) 이 row를 바닥으로 하는 경우의 최대 넓이 계산
            sorted_heights = sorted(heights, reverse=True)

            for width, h in enumerate(sorted_heights, start=1):
                ans = max(ans, h * width)

        return ans
