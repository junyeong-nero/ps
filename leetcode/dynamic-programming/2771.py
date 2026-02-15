class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        dp1 = dp2 = 1
        res = 1
        
        for i in range(1, n):
            new_dp1 = 1
            new_dp2 = 1
            
            # nums1[i] 선택
            if nums1[i] >= nums1[i - 1]:
                new_dp1 = max(new_dp1, dp1 + 1)
            if nums1[i] >= nums2[i - 1]:
                new_dp1 = max(new_dp1, dp2 + 1)
            
            # nums2[i] 선택
            if nums2[i] >= nums1[i - 1]:
                new_dp2 = max(new_dp2, dp1 + 1)
            if nums2[i] >= nums2[i - 1]:
                new_dp2 = max(new_dp2, dp2 + 1)
            
            dp1, dp2 = new_dp1, new_dp2
            res = max(res, dp1, dp2)
        
        return res



        # res = 0

        # @cache
        # def dfs(cur, prev=0, length=0):
        #     nonlocal res
        #     res = max(res, length)

        #     if cur == n:
        #         return
        #     dfs(cur + 1, nums1[cur], (length + 1) if nums1[cur] >= prev else 1)
        #     dfs(cur + 1, nums2[cur], (length + 1) if nums2[cur] >= prev else 1)

        # dfs(0, 0, 0)
        # return res

        # non decreasing arr[i] <= arr[i + 1]
        # choose always minimum elements?

        # arr = [float("-inf")]
        # res = 0
        # length = 0

        # for i in range(n):
        #     prev = arr[-1]
        #     if nums1[i] >= prev and nums2[i] >= prev:
        #         arr.append(min(nums1[i], nums2[i]))
        #         length += 1
        #     elif nums1[i] >= prev:
        #         arr.append(nums1[i])
        #         length += 1
        #     elif nums2[i] >= prev:
        #         arr.append(nums2[i])
        #         length += 1
        #     else:
        #         arr.append(min(nums1[i], nums2[i]))
        #         length = 1
        #     res = max(res, length)

        # print(arr)
        # return res





