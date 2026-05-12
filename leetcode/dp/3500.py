# class Solution:
#     def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:

#         n = len(nums)

#         # understanding:
#         # - nums and cost with n
#         # - divide into subarrays, cost = sum(nums[0...r] + k * i) * sum(cost[l ... r])
#         # cost = sum(nums[0...l) * sum(cost[l...r]) + k * i * sum(cost[l...r])
#         # how to minimize cost?
#         #

#         # design:
#         # - DP approach?
#         # - dp[i] : minimal total cost and # of subarrays with nums]

#         # time complexity
#         # - O(n)

#         prefix_nums = [0]
#         prefix_cost = [0]

#         # prefix_nums[i] = sum(nums[0...i])

#         for i in range(n):
#             prefix_nums.append(prefix_nums[-1] + nums[i])
#             prefix_cost.append(prefix_cost[-1] + cost[i])

#         print(prefix_nums)
#         print(prefix_cost)

#         dp = [(float("inf"), 0) for _ in range(n + 1)]
#         dp[0] = (0, 0)

#         for r in range(1, n + 1):
#             temp = min(
#                 [
#                     (
#                         dp[l][0]
#                         + (prefix_nums[r] + k * (dp[l][1] + 1))
#                         * (prefix_cost[r] - prefix_cost[l]),
#                         dp[l][1] + 1
#                     )
#                     for l in range(r)
#                 ]
#             )
#             dp[r] = min(dp[r], temp)

#         return dp[-1][0]


from typing import List


class Solution:
    def minimumCost(self, nums: List[int], cost: List[int], k: int) -> int:
        n = len(nums)

        prefix_nums = [0] * (n + 1)
        prefix_cost = [0] * (n + 1)

        for i in range(n):
            prefix_nums[i + 1] = prefix_nums[i] + nums[i]
            prefix_cost[i + 1] = prefix_cost[i] + cost[i]

        total_cost = prefix_cost[n]

        INF = float("inf")
        dp = [INF] * (n + 1)
        dp[0] = 0

        for r in range(1, n + 1):
            for l in range(r):
                segment_cost = prefix_nums[r] * (prefix_cost[r] - prefix_cost[l])

                if l == 0:
                    split_penalty = 0
                else:
                    split_penalty = k * (total_cost - prefix_cost[l])

                dp[r] = min(dp[r], dp[l] + segment_cost + split_penalty)

        return dp[n] + k * total_cost

