class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:

        n = len(nums)

        prefix = [0] * (n + 1)
        suffix = [0] * (n + 1)
        
        # 1. 왼쪽에서부터의 누적 OR 계산
        for i in range(n):
            prefix[i + 1] = prefix[i] | nums[i]
            
        # 2. 오른쪽에서부터의 누적 OR 계산
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] | nums[i]
            
        ans = 0
        # 3. 각 숫자 i에 k번의 연산을 몰아주는 경우를 모두 확인
        for i in range(n):
            # (i 이전까지의 OR) | (현재 숫자 << k) | (i 이후부터의 OR)
            current_or = prefix[i] | (nums[i] << k) | suffix[i + 1]
            ans = max(ans, current_or)
            
        return ans

        # dp[i][used] = nums[:i] with used op

        # dp = [[0] * (k + 1) for _ in range(n + 1)]
        # for i in range(1, n + 1):
        #     for j in range(k + 1):
        #         for p in range(k - j + 1):
        #             dp[i][j + p] = max(dp[i][j + p], dp[i - 1][j] | (nums[i - 1] << p))

        # # print(dp)
        # return dp[-1][-1]
         
        # @cache
        # def dfs(cur, used=0, value=0):

        #     if cur == n:
        #         return value

        #     res = float("-inf")
        #     res = max(res, dfs(cur + 1, used, value | nums[cur]))
        #     for i in range(1, k - used + 1):
        #         res = max(res, dfs(cur + 1, used + i, value | (nums[cur] << i)))
        #     return res

        # res = dfs(0)
        # return res
