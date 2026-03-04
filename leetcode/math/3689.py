from typing import List

class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        return (max(nums) - min(nums)) * k
#         n = len(nums)
#         # choose k subarrays and value = max(sub-arr) - min(sub-arr)
#         # maximize total value

#         # 1. sorted with max(sub-arr) - min(sub-arr)
#         # 2. select k sub-arr from above

#         # constraints : n <= 5 * 10^4
#         # o (n log n)

#         # max-heap
#         nums = sorted([(num, index) for index, num in enumerate(nums)])
#         i = 0
#         j = n - 1

#         # 3 1 9 4
#         #   ^ ^ 
#         #   1 2
#         # 2 * (4 - 2)

#         size = 0
#         res = 0

#         while True:
            
#             start, end = min(nums[i][1], nums[j][1]), max(nums[i][1], nums[j][1])
#             prob = (start + 1) * (n - end)
#             res += min(k - size, prob) * (nums[j][0] - nums[i][0])
#             size += min(k - size, prob)

#             if size == k:
#                 break
#             if nums[j][0] - nums[i + 1][0] > nums[j - 1][0] - nums[i][0]:
#                 i += 1
#             else:
#                 j -= 1

#         return res
