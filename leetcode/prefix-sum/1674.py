from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            low = min(a, b) + 1
            high = max(a, b) + limit
            s = a + b

            # 기본적으로 모든 target sum은 2 moves 필요
            diff[2] += 2
            diff[2 * limit + 1] -= 2

            # low ~ high 구간은 1 move로 가능하므로 -1
            diff[low] -= 1
            diff[high + 1] += 1

            # 정확히 s에서는 0 move 가능하므로 추가로 -1
            diff[s] -= 1
            diff[s + 1] += 1

        ans = float("inf")
        cur = 0

        for target in range(2, 2 * limit + 1):
            cur += diff[target]
            ans = min(ans, cur)

        return ans
