from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        # Track the best length among all valid subarrays.
        max_len = 0

        # Try every start index i.
        for i in range(len(nums)):
            # odd/even maps store frequency of distinct odd/even values.
            odd = {}
            even = {}

            # Expand subarray [i..j].
            for j in range(i, len(nums)):
                if nums[j] & 1:
                    odd[nums[j]] = odd.get(nums[j], 0) + 1
                else:
                    even[nums[j]] = even.get(nums[j], 0) + 1

                # Balanced when distinct odd count == distinct even count.
                if len(odd) == len(even):
                    max_len = max(max_len, j - i + 1)

        return max_len
