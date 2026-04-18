class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        
        n = len(nums)
        nums_r = [int(str(num)[::-1]) for num in nums]
        d = dict()
        res = n

        for i in range(n):
            if nums[i] in d:
                res = min(res, i - d[nums[i]])
            d[nums_r[i]] = i

        # print(nums_r)
        # print(d)

        return res if res < n else -1
