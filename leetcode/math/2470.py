class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        
        # number of subarray of nums s.t. least common multiple of subarray == k
        # n <= 10^3
        # solve in O(n^2)
        # sliding window?

        n = len(nums)
        res = 0

        # O(n^2)
        for i in range(n):

            value = 1
            for j in range(i, -1, -1):
                value = lcm(value, nums[j])
                if value == k:
                    res += 1
                if value > k or k % value != 0:
                    break

        return res

