from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        a = sorted(nums1)
        b = sorted([(v, i) for i, v in enumerate(nums2)])  # (value, original_index)

        ans = [0] * n
        lo, hi = 0, n - 1  # pointers on a

        # assign from largest nums2 to smallest
        for v, idx in reversed(b):
            if a[hi] > v:
                ans[idx] = a[hi]
                hi -= 1
            else:
                ans[idx] = a[lo]
                lo += 1

        return ans


# class Solution:
#     def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:

#         n = len(nums1)
#         a, b = sorted(nums1), sorted(zip(nums2, range(n)))

#         def shift_advantages(shift=0):
#             # nums1 : 1 2 3 4
#             # nums2 : <---> 3 4 5 6
#             # advantages: 1 with shift = 3

#             count = 0
#             arr = []
#             for i in range(n):
#                 p = a[(i + shift) % n]
#                 q = b[i][0]
#                 if p > q:
#                     count += 1
#                 arr.append((b[i][1], p))

#             arr.sort()
#             arr = [elem[1] for elem in arr]
#             return count, arr

#         left, right = 0, n
#         while left <= right:
#             mid = (left + right) // 2
#             if shift_advantages(mid)[0] < shift_advantages(mid + 1)[0]:
#                 left = mid + 1 
#             else:
#                 right = mid - 1

#         return shift_advantages(left)[1]
