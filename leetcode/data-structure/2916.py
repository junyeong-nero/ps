class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        # distinct values between [i...j]
        MOD = 10 ** 9 + 7
        n = len(nums)

        # dp[i][j] : sum of squares of distnct values in nums[i...j]
        # n = 10^5
        
        dp = [0 for _ in range(n)] 
        dp[0] = 1

        d = defaultdict(list)
        d[nums[0]].append(0)

        def func0(i):
            temp = 0
            d = set()
            for j in range(i, -1, -1):
                d.add(nums[j])
                temp += len(d) ** 2
            return temp

        for i in range(1, n):
            num = nums[i]
            dp[i] = dp[i - 1] + func0(i)
            d[num].append(i)

        print(dp)
        return dp[-1] % MOD

        # 12
        # k = 1

        # number of subsets which contains nums[i] -> same value * 2
        # number of subsets which does not contain nums[i] -> 2^k - 1 ->

        # sub array! -> continuous
        
        # - kC1 + kC2 ... kCk = 2^k - 1
        # + kC1 * (2^2 - 1^1) + kC2 * (3^2 - 2^2) ... kCk * (k + 1)^2 - k^2
        # [1, 2, 3, 1] -> [1, 2, 3] [1] 
