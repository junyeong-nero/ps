from typing import List
from bisect import bisect_right

class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)

        arr = sorted(zip(costs, capacity))

        # prefix[i] = arr[0] ~ arr[i-1] 중 최대 capacity
        prefix = [0]
        for c, cap in arr:
            prefix.append(max(prefix[-1], cap))

        res = 0

        # 머신 1개만 고르는 경우: cost < budget
        one_limit = bisect_right(arr, budget - 1, key=lambda x: x[0])
        res = max(res, prefix[one_limit])

        # 머신 2개 고르는 경우
        for i in range(n):
            cost_i, cap_i = arr[i]

            # partner cost <= budget - cost_i - 1
            limit = budget - cost_i - 1

            # partner는 i보다 앞에 있어야 distinct 보장
            j = bisect_right(arr, limit, key=lambda x: x[0])
            j = min(j, i)

            if j > 0:
                res = max(res, prefix[j] + cap_i)

        return res
