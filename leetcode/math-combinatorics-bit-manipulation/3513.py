class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        # ordering is matter
        # let x = nums[i] XOR nums[j] XOR nums[k] where i <= j <= k
        #  - but A XOR B = B XOR A,  ==> i, j, k ordering is not matter
        # pick any index i, j, k and XOR .
        if n <= 2:
            return n
        return 2 ** (int(log(n, 2)) + 1)
