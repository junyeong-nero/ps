class Solution:
    def minStable(self, nums: List[int], maxC: int) -> int:

        count1 = 0
        for i in nums:
            if i == 1:
                count1 += 1
        if count1 + maxC >= len(nums):
            return 0

        @cache
        def hcf(a, b):
            while a % b:
                a, b = b, a % b
            return b

        def caclulate_bound_array():
            bounds_array = [-1 for i in nums]
            idx_mapping = dict()
            for idx, val in enumerate(nums):
                temp = dict()
                temp[val] = idx
                if val != 1:
                    for val2, idx2 in idx_mapping.items():
                        curr_hcf = hcf(val2, val)
                        temp[curr_hcf] = max(idx2, temp.get(curr_hcf, -1))
                bounds_array[idx] = temp.get(1, -1)
                idx_mapping = temp
            return bounds_array

        bounds_array = caclulate_bound_array()

        def check2(window_size, operations):
            last_updated_at = -1
            for idx, val in enumerate(bounds_array):
                if (
                    idx - last_updated_at > window_size
                    and idx - bounds_array[idx] > window_size
                ):
                    if not operations:
                        return False
                    operations -= 1
                    last_updated_at = idx
            return True

        low = 1
        high = max(idx - val for idx, val in enumerate(bounds_array))
        while low < high:
            mid = (low + high) // 2
            if check2(mid, maxC):
                high = mid
            else:
                low = mid + 1
        return low


# class Solution:
#     def minStable(self, nums: List[int], maxC: int) -> int:
#         # stable : highest common factor ? >= 2 of all elements
#         # longest stable subarray
#         # can modify maxC elements
#         # minimum stable factor?

#         # dp[i][j][k] : nums[i:j] 에서 maxC 수정을 했을 때 가질 수 있는 ...
#         # 소수가 문제다. 이 녀석들 들어가면 subarray 가 될 수 없고 끊긴다.

