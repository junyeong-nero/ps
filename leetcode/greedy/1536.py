class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        # valids. swap two adjacent rows.
        n = len(grid)

        def count_leading_zeros(arr):
            count = 0
            for num in arr[::-1]:
                if num == 0:
                    count += 1
                else:
                    break
            return count

        rows = [count_leading_zeros(row) for row in grid]
        # rows = sorted(rows, key=itemgetter(0), reverse=True)
        # h

        steps = 0

        for i in range(n):
            target = n - 1 - i
            if rows[i] >= target:
                continue

            j = i + 1
            while j < n and rows[j] < target:
                j += 1

            if j == n:
                return -1

            temp = rows[j]
            del rows[j]

            steps += j - i
            rows.insert(i, temp)

            # print(rows)

        return steps

