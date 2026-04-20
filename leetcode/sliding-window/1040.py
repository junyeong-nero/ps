from functools import lru_cache


class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        # endpoint stone -> no endpoint stone
        # three consecutive positions

        n = len(stones)
        stones.sort()

        # print(stones)

        min_value, max_value = n, float("-inf")

        arr = []
        for i in range(n - 1):
            if stones[i + 1] - stones[i] <= 2:
                min_value -= 1
            max_value = max(max_value, stones[i + 1] - stones[i] - 1)

        return [min_value, max_value]

        # print(q)
        # (3, 2) -> (1, 2) [4, 5, 7]
        #                   -> (1, 1)
        #        -> (1, 1) [7, 8, 9] (end)

        # 1, 5, 10, 16
        # 4,5,6 -> (1,4,6) / (2,3,6) / (3,2,6) / (4,1,6) [5,6,10,16] ~ [5,9,10,16]
        #       -> (1,3) / ()

        min_value, max_value = float("inf"), float("-inf")
        memo = dict()

        def dfs(step=0):

            nonlocal arr, min_value, max_value

            if set(arr) == {1}:
                min_value = min(min_value, step)
                max_value = max(max_value, step)
                return

            for i in range(1, len(arr)):
                A, B = arr[i], arr[i - 1]

                for a in range(1, A):
                    arr[i - 1], arr[i] = a, A - a
                    dfs(step + 1)

                arr[i], arr[i - 1] = A, B

            for i in range(len(arr) - 1):
                A, B = arr[i], arr[i + 1]

                for a in range(1, A):
                    arr[i + 1], arr[i] = a, A - a
                    dfs(step + 1)

                arr[i], arr[i + 1] = A, B

        res = dfs(0)

        # dfs time complexity
        # O(n) * O(n) => too big!

        return [min_value, max_value]

        # 생각을 해보자.
        #         V   V
        #   ㅁ   ㅁ  ㅁ  ㅁ
        #   ^
        #  이 돌이 움직일 수 있는 범위는 여기로 갈 수 있음.
        #  결국 중요한건, 돌들 사이에 얼마나 공간이 있는지?

        # 1 3 5 7 9 -> (1) 을 옮긴다면 4, 6, 8
        #              (9) 를 옮긴다면 2, 4, 6

        # 3 4 5 7 9
        # 4 5 6 7 9
        # 5 6 7 8 9

        # 1, 3, 1000
        # min = 1
        # max = 1000

    def numMovesStonesII(self, A):
        A.sort()
        i, n, low = 0, len(A), len(A)
        high = max(A[-1] - n + 2 - A[1], A[-2] - A[0] - n + 2)
        for j in range(n):
            while A[j] - A[i] >= n:
                i += 1
            if j - i + 1 == n - 1 and A[j] - A[i] == n - 2:
                low = min(low, 2)
            else:
                low = min(low, n - (j - i + 1))
        return [low, high]

