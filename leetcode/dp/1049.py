class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # two stone -> x <= y : break x, y - x
        # smallest possible weight of left stone
        # fin

        # dp 아닌것 같음.
        # dp[i] : stones[:i] 를 사용했을 때 남은 stone의 최소값. -> 이걸로 stones[:i+1] 의 최소값을 구할 수 있나?
        # stones[i] > dp[i] 인 경우 -> stones[i] - dp[i] 가 최소?
        # stones 개수가 엄청 작네. 그냥 bruteforce 해도 될것 같은데
        # sorting 해도 안될 것 같고.

        # 결국 충돌은 n - 1 번 일어남
        # 한 번 충돌 할 때 n * n 개의 경우의 수가 있음. => n^3

        # 1, 1, 2, 4, 7, 8
        # (4 + 7) (1 + 1 + 2 + 8) = 11, 12 => 1

        # 21, 26, 31, (33, 40)

        n = len(stones)
        total = sum(stones)

        @cache
        def dfs(index, value):
            if index == n:
                return abs(total - 2 * value)

            res = float('inf')
            res = min(res, dfs(index + 1, value))
            res = min(res, dfs(index + 1, value + stones[index]))
            return res

        res = dfs(0, 0)
        return res
        
        # def dfs():
        #     nonlocal stones

        #     count = 0
        #     res = float("inf")

        #     for i in range(n):
        #         if stones[i] == float("inf"): 
        #             count += 1
        #             continue

        #         for j in range(i):
        #             if stones[j] == float("inf"): continue

        #             A, B = stones[i], stones[j]
        #             if A != B:
        #                 stones[i], stones[j] = max(A, B) - min(A, B), float("inf")
        #                 res = min(res, dfs())
        #                 stones[i], stones[j] = A, B
        #             else:
        #                 stones[i], stones[j] = float("inf"), float("inf")
        #                 res = min(res, dfs())
        #                 stones[i], stones[j] = A, B

        #     if count == n - 1:
        #         res = min(stones)

        #     return res

        # res = dfs()
        # return res



