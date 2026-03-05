from typing import List


class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        INF = 10**9

        keep = 0  # i-1까지, (i-1)을 swap 안함
        swap = 1  # i-1까지, (i-1)을 swap 함 (0에서 swap하면 1)

        for i in range(1, n):
            nk = ns = INF

            a0, b0 = nums1[i - 1], nums2[i - 1]
            a1, b1 = nums1[i], nums2[i]

            # 직진 조건
            if a1 > a0 and b1 > b0:
                nk = min(nk, keep)
                ns = min(ns, swap + 1)

            # 교차 조건
            if a1 > b0 and b1 > a0:
                nk = min(nk, swap)
                ns = min(ns, keep + 1)

            keep, swap = nk, ns

        return min(keep, swap)


# class Solution:
#     def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
#         # swap nums1[i] and nums2[i]
#         # 큰놈을 모두 nums1... 으로 보내면 안되는구나?
#         # 그럼 어떻게 해? BFS 로 풀자 그냥
#         # 그러기에는 배열 크기가 너무 긴데.. 사실 두 배열 모두 정렬이 되어야 해.
#         # dp[i]를 num1[:i], nums2[:i] 를 increasing 하게 만드는 최소 operations 라고 해보자.
#         # 약간 이상한게, 다음 정보를 알기 위해서는 마지막 인덱스의 값을 알아야 해.
#         # dp[0] = 0
#         # dp[k] = dp[k - 1] or (dp[k - 1] + 1) if need swaps at [i]

#         # swap 의 개수는 n / 2 개를 넘을 수 없어. 무조건 n - n / 2 보다 작은 op 안에 수행이 가능해.
#         # 일단 nums1[i] == nums2[i] 인 경우에도 swap 을 하지 않아도 돼.
#         # 일종의 greedy...? back tracking ?

#         n = len(nums1)


#         def dfs(i, step):
#             if i == n:
#                 return step

#             res = float("inf")
#             if nums1[i] == nums2[i] or i == 0:
#                 # 그대로 진행
#                 res = min(res, dfs(i + 1, step))
#             elif i - 1 >= 0 and nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
#                 # 그대로 진행
#                 res = min(res, dfs(i + 1, step))

#             # swap 후 진행
#             nums1[i], nums2[i] = nums2[i], nums1[i]
#             if i - 1 >= 0 and nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
#                 res = min(res, dfs(i + 1, step + 1))
#             nums1[i], nums2[i] = nums2[i], nums1[i]

#             return res

#         res = dfs(0, 0)
#         return res

